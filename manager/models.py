from pymongo import MongoClient
from configparser import ConfigParser 

global db_mongo

configur = ConfigParser() 
configur.read('./config.ini') 

connect_link = configur.get('connect','DB_CONNECTION_LINK')
try:
    cluster = MongoClient(str(connect_link))
except:
    print("Cannot Connect to Internet...")
    
db_mongo= cluster["ealpha4test"]