import requests
import json

# 定义GraphQL查询
query = """
{
  approvals(first: 1) {
    id
    owner
    approved
    tokenId
  }
  approvalForAlls(first: 1) {
    id
    owner
    operator
    approved
  }
}
"""

# 设置API端点
url = "https://api.studio.thegraph.com/query/81617/pudgypenguins-/v0.0.1"

# 设置请求头
headers = {
    "Content-Type": "application/json"
}

# 发送POST请求
response = requests.post(url, headers=headers, json={"query": query})

# 检查响应状态码
if response.status_code == 200:
    # 解析响应JSON数据
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Query failed to run by returning code of {response.status_code}. {response.text}")
