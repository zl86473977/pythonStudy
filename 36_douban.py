from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# response = requests.get("https://movie.douban.com/top250", headers=headers)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")

# titleDivs = soup.findAll("div", attrs={"class": "hd"})
# for title in titleDivs:
#     titleA = title.find("a")
#     titleSpan = titleA.find("span")
#     print(titleSpan.string)

# all_titles = soup.findAll("span", attrs={"class": "title"})
# for title in all_titles:
#     title_string = title.string
#     if "/" not in title_string:
#         print(title_string)

startNum = 0
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)