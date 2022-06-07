import json

ip_group = dict()

user1 = dict()
user1["ip_addr"] = "192.168.100.1"
ip_group["USER1"] = user1

with open('D:\github_task\server_script\json-macro\ip_addr.json', 'w', encoding='utf-8') as make_file :
    json.dump(user1, make_file, indent="\t")
    
with open('D:\github_task\server_script\json-macro\ip_addr.json', 'r') as f :
    json_data = json.load(f)

print(json.dumps(json_data, indent="\t"))