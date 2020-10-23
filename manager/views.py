from django.shortcuts import render,redirect
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
import itertools 
from bson import ObjectId

# Create your views here.
def managerlogin(request):
    print("im in get method")
    if request.session.has_key('admin'):
        adminID = request.session['admin']
        return redirect('manager') 
    else:
        if request.method == 'POST':
            print("im in post method")
            adminID = request.POST['AdminID']
            password = request.POST['Password']
            
            
            admin_data = db_mongo['manager_data']
            admin_data_retrived = admin_data.find({})
            print(admin_data_retrived)
            
            for item in admin_data_retrived:
                admin_ID_db = item['manager_admin_ID']
                admin_password_db = item['password']
            Admin_pass_check = check_password_hash(admin_password_db,password)
            
            
            
            
            if admin_ID_db == adminID and Admin_pass_check == True:
                print("Admin authenticated..")
                request.session['admin'] = admin_ID_db
                return redirect('manager') 
            else:
                print("Authentication Failed.")
                return render(request,"manager/managerlogin.html",{'pop_up':"error"})
            return render(request,"manager/managerlogin.html",{'pop_up':"error"})
        return render(request,"manager/managerlogin.html",{'pop_up':"entry"})



def manager(request):
    if request.method == 'POST':
            print("im in post method")
            statusoptions = request.POST['statusoptions']
            print(statusoptions)
    if request.session.has_key('admin'):
        adminID = request.session['admin']

        post_data_db = db_mongo['post_data_db']
        users_array_filt =[]
        data_u = []
        post_data = []
        post_data_db_retrived = post_data_db.find({}).sort([( '$natural', -1 )] )
        
        count = 0
        for item in post_data_db_retrived:
            count=count+1
            for key,value in item['users'].items():
                if value == "Enable":
                    data_u.append(key)
            data={
                "_id":item['_id'],
                "task":item['task'],
                "taskstatus":item['taskstatus'],
                "userdata":data_u,
                "count":count
            }
            data_u = []
            post_data.append(data)
            
        # print(post_data)
        return render(request,"manager/manager.html",{"post_data_db_retrived":post_data})
    return render(request,"manager/managerlogin.html")


def manager_logout(request):
    if request.session.has_key('admin'):
        print("The admin is being logged out")
        del request.session['admin']
    return redirect("welcome")



def edit(request): 
    if request.method == 'POST':
        data_users_arr = []
        state_users_arr = []
        
        taskname = request.POST['statusoptions']
        print(taskname)
        post_data_db = db_mongo['post_data_db']
        edit_post_query = post_data_db.find_one({"task":taskname})
        taskname_full = edit_post_query["task"]
        unique_id = edit_post_query["_id"]
        taskname_Status = edit_post_query["taskstatus"]
        
        for key,value in edit_post_query['users'].items():
                # if value == "Enable":
            data_users_arr.append(key)
            state_users_arr.append(value)
        
 
        
        users_array=[]
        count = 0
        user_data_E = db_mongo['users']
        user_data_retrived = user_data_E.find({})
        
        for item,state_f,username in zip(user_data_retrived,state_users_arr,data_users_arr):
            #print(username,item["username"])
            if username == item["username"]:
                count = count+1
                data = {"username":item["username"],
                "email":item["Email"],
                "name":item["name"],
                "count":count,
                "state":state_f
                }
                users_array.append(data)
        
        return render(request,"manager/manageredit.html",{'taskname_full':taskname_full,
                                                          "taskname_Status":taskname_Status,
                                                          "data_users_arr":data_users_arr,
                                                          "state_users_arr":state_users_arr,
                                                          "users_array":users_array,
                                                          'unique_id':unique_id})
    return render(request,"manager/manageredit.html")

def edit_post_request_method(request):
    if request.method == 'POST':
        users_data_ED = {}
        print("Im in edit_post_request_method post method")
        unique_id = request.POST['unique_id']
        taskname = request.POST['taskname']
        statusoptions = request.POST['statusoptions']
        print(taskname)
        print(statusoptions)
        
        user_data_edit = db_mongo['users']
        user_data_retrived_edit = user_data_edit.find({})
        
        for item in user_data_retrived_edit:
            username = item["username"]
            userstate = request.POST[username]
            users_data_ED[username] = userstate
        
        print(users_data_ED)
        
        post_data = {
            "task": taskname,
            "taskstatus": statusoptions,
            "users": users_data_ED 
        }
        
        
        post_data_db_edit = db_mongo['post_data_db']
        post_data_db_edit.update_one({"_id":ObjectId(unique_id)},{"$set":{"task":taskname,
                                                                    "taskstatus":statusoptions,
                                                                    "users":users_data_ED}})
    
        print("post updated successfully..")
        return redirect('manager')
    return redirect('manager')
        
        
def create(request):
    if request.method == 'POST':
        users_data_ED = {}
        print("Im in Create post method")
        taskname = request.POST['taskname']
        statusoptions = request.POST['statusoptions']
        
        
        user_data = db_mongo['users']
        user_data_retrived = user_data.find({})
        
        for item in user_data_retrived:
            username = item["username"]
            userstate = request.POST[username]
            users_data_ED[username] = userstate
            
        post_data = {
            "task": taskname,
            "taskstatus": statusoptions,
            "users": users_data_ED 
        }
        
        post_data_db = db_mongo['post_data_db']
        post_data_db.insert_one(post_data)
        return redirect('manager')
        
        
    if request.method == 'GET':
        users_array = []
        count = 0
        user_data = db_mongo['users']
        user_data_retrived = user_data.find({})
        
        for item in user_data_retrived:
            count = count+1
            data = {"username":item["username"],
             "email":item["Email"],
             "name":item["name"],
             "count":count
             }
            users_array.append(data)
        
        return render(request,"manager/managercreate.html",{'users_array' : users_array})
    return render(request,"manager/managercreate.html")  


