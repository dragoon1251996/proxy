import redis
import json
import re
r = redis.Redis(host='localhost', port=6379, db=0)
line=[x.replace("\n","") for x  in open("v.json",encoding="utf-8")]

for x in line:
    if "host" in x:
        print(x)
        r.set(re.findall("\'(.*?)\'",x)[0],eval(re.findall("\':(.*?)}",x)[0]+"}"))

# for key in r.scan_iter("*"):
#     # delete the key
#     print(key)