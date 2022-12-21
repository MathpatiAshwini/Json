import json
a={"a":"archana","b":"tammna","c":"ashwini"}
with open("a.json","w") as json_file:
    json.dump(a,json_file)
