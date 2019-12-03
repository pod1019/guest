import requests
# 查询发布会接口
url = "http://127.0.0.1:8001/api/get_event_list/"
r = requests.get(url,params={'eid':'1'})
print(type(r))

result = r.json()
print(result)
print(type(result))

assert result['status']==200
assert result['message'] == "success"
assert result['data']['name'] == "华为 P90 发布会"
assert result['data']['address'] == "国家体育馆"
assert result['data']['start_time'] == '2019-12-22T10:30:00'
