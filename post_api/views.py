from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *


class main_api(APIView):
    def get(self,request, **kwargs):
        username = self.kwargs['username']
        print("in the API method")
        print(username)
        user_name = username
        user_name_db_data = db_mongo['users']
        person_record = user_name_db_data.find({'username' : user_name})
        for param in person_record:
            user_name_disp = param["name"]
        
        post_data_db = db_mongo['post_data_db']
        data_u = []
        post_data = []
        checked_array=[]
        query = "users."+str(user_name)
        person_post_record = post_data_db.find({query : "Enable"})
        for item in person_post_record:
            count = 0
            count=count+1
            for key,value in item['users'].items():
                if value == "Enable":
                    data_u.append(key)
                    
                if item['taskstatus'] == "Initiated":
                    checked_array = ["active", "", "", ""]
                elif item['taskstatus'] == "In_Progress":
                    checked_array = ["", "active", "", ""]
                elif item['taskstatus'] == "Completed":
                    checked_array = ["", "", "active", ""]
                elif item['taskstatus'] == "Delayed":
                    checked_array = ["", "", "","active"]
                    
            data={
                "task":item['task'],
                "taskstatus":item['taskstatus'],
                "userdata":data_u,
                "count":count,
                "checked_array":checked_array
            }
            data_u = []
            checked_array=[]
            post_data.append(data)
            
        jsondata = {"post_data_db_retrived":post_data,
                    "user_name_disp":user_name_disp}
        
        #print(jsondata)
        return Response(jsondata)
    
    def post(self,username):
        pass
