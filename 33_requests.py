import requests
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get("http://books.toscrape.com/", headers=head)
print(response)
if response.ok:
    print(response.text)
else:
    print("请求失败")