from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient('localhost', 27017)

db = client.bit
col = db.student

mydoc = {"name":"홍길동","age":20}
print(mydoc)


#s = { "name":"김슬지","kor":"100", "eng":"90" , "math":"80"}
s =col.find({})
#for s in col.find({},{"_id":0}):
    #print(s)

for r in col.find({"kor":{"$gt":80}},{"_id":0, "name":1, "kor":1}):
    #print(r)
    re = dumps(r, ensure_ascii=False)
    print(re)
