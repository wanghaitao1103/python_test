import requests
import os
from dotenv import load_dotenv

# 目标 API 网址
url = "https://api.github.com/user"

# ==========================================
# 测试 1：不带 Token (预期返回 401 Unauthorized)
# ==========================================
print("--- 测试 1：无 Token (401 模拟) ---")

# 发送 GET 请求（相当于 Java 里的 HttpClient.send）
response_no_auth = requests.get(url)

print(f"HTTP 状态码: {response_no_auth.status_code}")
print(f"服务器返回信息: {response_no_auth.json()}\n")


# ==========================================
# 测试 2：带 Token (预期返回 200 OK)
# ==========================================
print("--- 测试 2：带 Token (200 模拟) ---")

#  将这里的字符串替换为你刚刚在 GitHub 生成的真实 token
# 1. 加载 .env 文件中的变量到操作系统的环境变量中
load_dotenv()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Python 的字典 (Dictionary)，相当于 Java 里的 HashMap<String, String>
# 我们用它来构造 HTTP 请求头 (Headers)
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}", 
    "Accept": "application/vnd.github+json",     # 推荐的 GitHub API 规范
    "X-GitHub-Api-Version": "2022-11-28"         # 指定 API 版本
}

# 发送带有 headers 的 GET 请求
response_auth = requests.get(url, headers=headers)

print(f"HTTP 状态码: {response_auth.status_code}")

if response_auth.status_code == 200:
    # .json() 会自动将返回的 JSON 字符串转为 Python 字典（相当于 Java 里的反序列化为 Map）
    user_data = response_auth.json() 
    print("认证成功！")
    print(f"你的 GitHub 用户名是: {user_data.get('login')}")
    print(f"你的公开仓库数量是: {user_data.get('public_repos')}")
else:
    print(f"请求失败: {response_auth.json()}")