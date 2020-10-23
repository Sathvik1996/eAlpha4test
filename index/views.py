from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import db_mongo
from werkzeug.security import generate_password_hash, check_password_hash
# Create your views here.

def welcome(request):
    if request.session.has_key('admin'):
        return redirect('manager') 
    if request.session.has_key('user'):
        return redirect('userprofile') 
    return render(request,"welcome.html")


def login(request):
    if request.method == 'POST':
        print("Im in login post method")
        username = request.POST['username']
        password = request.POST['password']
        
        user_data = db_mongo['users']
        Personlogindata_usr = user_data.find_one({"username": username})
        
        # state = Personlogindata_usr["state"]
        
        if (Personlogindata_usr!=None):
            password_check_usr = check_password_hash(Personlogindata_usr["password"],password)
            if (Personlogindata_usr!=None and password_check_usr==True  ) :
                request.session['user'] = username
                return redirect('userprofile')
            else:
                return render(request,"user/login.html",{'pop_up':"error"})
        else:
            print("Username/Password  Not Matched")
            return render(request,"user/login.html",{'pop_up':"error"})
    if request.method == 'GET':
        return render(request,"user/login.html",{'pop_up':"startup"})
        
        
        
         
    
    

def register(request):
    if request.method == 'POST':
        print("Im in register post method")
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(username,password,first_name,email)
        
        
        user_data = db_mongo['users']
        PersonREGdata_usr = user_data.find_one({"username": first_name})
        if (PersonREGdata_usr!=None):
            return render(request,"register.html")
        else:
            Full_count = user_data.find().count()
            Reg_Dict = { "siid":Full_count+1,
                    "name":first_name,
                    "Email":email,
                    "username":username,
                    "password":generate_password_hash(password),
                    "state":"Disable"}
            user_data.insert_one(Reg_Dict)
            return render(request,"register.html")
        
    return render(request,"register.html")
    
@csrf_exempt
def userprofile(request):
    pop_up = "startup"
    if request.method == 'POST':
        print("im in userprofile post method...")
        statusoptions = request.POST['statusoptions']
        statusoptions = statusoptions.split("$")
        statusoptions_state = statusoptions[0]
        task_name_post = statusoptions[1]
        
        post_data_db_f = db_mongo['post_data_db']
        post_data_db_f.update({"task" : task_name_post}, {"$set" : {"taskstatus" :statusoptions_state}})
        print("Successfully Changed")
        pop_up = "success"
        
        
    if request.session.has_key('user'):
        user_name_unique = request.session['user']
        user_name_db_data = db_mongo['users']
        person_record = user_name_db_data.find({'username' : user_name_unique})
        user_name=user_name_unique
        for param in person_record:
            user_name_disp = param["name"]
            #print(user_name_disp)
        
        post_data_db = db_mongo['post_data_db']
        data_u = []
        post_data = []
        
        
        query = "users."+str(user_name)
        person_post_record = post_data_db.find({query : "Enable"})
        for item in person_post_record:
            #print (item)
            count = 0
            count=count+1
            for key,value in item['users'].items():
                if value == "Enable":
                    data_u.append(key)
            data={
                "task":item['task'],
                "taskstatus":item['taskstatus'],
                "userdata":data_u,
                "count":count
                
            }
            data_u = []
            post_data.append(data)
            
        print(user_name_unique)
    return render(request,"user/userprofile.html",{"post_data_db_retrived":post_data,
                                                    "user_name_disp":user_name_disp,
                                                    'pop_up':pop_up,
                                                    'user_name_unique':user_name_unique})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return render(request,"user/userprofile.html")

def user_logout(request):
    if request.session.has_key('user'):
        del request.session['user']
    return render(request,"welcome.html")