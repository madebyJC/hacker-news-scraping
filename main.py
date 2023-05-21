# from bs4 import BeautifulSoup
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())
#
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_is_heading = soup.find_all(classs_="heading")
# print(class_is_heading)
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

# ---------------------------------------------------------------

# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
#
# print(response.text)

# ---------------------------------------------------------------
# https://news.ycombinator.com/news

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
