# redis-server (start redis-server)
# redis-cli flushall (delete all keys)

import redis
import json

r = redis.StrictRedis(host='localhost', decode_responses=True, port=6379, db=0)

def json_in(json_file):
    with open(json_file, 'r') as f:
        for data in f.readlines():
            jdata = json.loads(data)
            dic = {}
            for j in jdata:
                if j != 'tag':
                    dic[j] = jdata[j]
            r.hmset(jdata['tag'],dic)

json_in("pearson.json")
json_in("week_predict.json")
json_in("df_dif.json")
json_in("df_dem.json")
json_in("df_osc.json")
json_in("weather_logical_Q3.json")
