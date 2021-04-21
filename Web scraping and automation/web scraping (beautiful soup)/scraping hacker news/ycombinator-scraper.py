from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
ycombinator_web_page = response.text
# print(ycombinator_web_page)
ycombinator_soup = BeautifulSoup(ycombinator_web_page, "html.parser")
# to get the links on the website that are related to the posted stories
articles = ycombinator_soup.find_all(name= "a", class_= "storylink")
# savint the posts with their index as keys,and the value of a dictionary
# this dictionary contains the articles texts as keys and their links as values  that
posts={index:{article_tag.getText():article_tag.get("href")} for index,article_tag in enumerate(articles) }
print(posts)
scores=[score for score in ycombinator_soup.find_all(name= "span",class_= "score")]
# print(f"scores{scores}")
article_upvotes = [int(score.getText().split()[0]) for score in ycombinator_soup.find_all(name= "span",
                                                                                          class_= "score")]
print(article_upvotes)
highest_votes=posts[article_upvotes.index(max(article_upvotes))]
print(f"Highest votes{highest_votes}")
