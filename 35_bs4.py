from bs4 import BeautifulSoup
import requests
content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")
# class 和 属性 筛选出想要的标签
all_prices = soup.findAll("p", attrs={"class": "price_color"})
for price in all_prices:
    # print(price)  # <p class="price_color">Â£51.77</p>
    # print(price.string)  # Â£51.77
    print(price.string[2:])  # 51.77

all_titles = soup.findAll("h3")
for title in all_titles:
    # all_links = title.findAll("a")
    # for link in all_links:
    #     print(link.string)
    # link = title.find("a")
    # print(link.string)
    print(title)