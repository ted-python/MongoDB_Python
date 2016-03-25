'''
https://docs.mongodb.org/getting-started/python/
'''

from pymongo import  MongoClient
client = MongoClient("mongodb://root:root@ds025379.mlab.com:25379/lumin")
db=client['lumin']
users=db.users
cursor=users.find()
for document in cursor:
    print document
print "--------------------------------------------------------------------------"
print "--------------------------------------------------------------------------"

cursor_1=users.find({"username":"mkyong"  })
for document in cursor_1:
    print document

print "--------------------------------------------------------------------------"
print "--------------------------------------------------------------------------"




