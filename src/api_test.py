import requests

url = "https://api.github.com/users/torvalds"
response = requests.get(url)

# 解析响应
if response.status_code == 200:
    data = response.json()
    print("用户名:", data["login"])
    print("打印数量:", data["followers"])
    print(data)
    
else:
    print("请求失败，状态码:", response.status_code)