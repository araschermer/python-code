from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
ycombinator_web_page = response.text
# print(ycombinator_web_page)
ycombinator_soup = BeautifulSoup(ycombinator_web_page, "html.parser")
# to get the links on the website that are related to the posted stories
articles = ycombinator_soup.find_all(name="a", class_="storylink")

# saving the posts with their index as keys,and the value of a dictionary
# this dictionary contains the articles texts as keys and their links as values  that
posts = {index: {article_tag.getText(): article_tag.get("href")} for index, article_tag in enumerate(articles)}
print(posts)

#  getting the story with the most upvote score #
scores = [score for score in ycombinator_soup.find_all(name="span", class_="score")]
# print(f"scores{scores}")

#  get all upvote scores
articles_upvote_scores = [int(score.getText().split()[0]) for score in ycombinator_soup.find_all(name="span",
                                                                                                 class_="score")]
# print(articles_upvote_scores)
#  get the article with the maximum upvote count

highest_votes = max(articles_upvote_scores)
article_with_highest_votes = posts[articles_upvote_scores.index(highest_votes)]
for title, link in article_with_highest_votes.items():
    print(f"Article with the highest upvote count:\n Title:{title}\nlink: {link}")

# getting the top 3 articles
# getting hold of the 3 top scores
top_3_articles = sorted(articles_upvote_scores, reverse=True)[:3]
for article_score in top_3_articles:
    # getting the articles  with the 3 highest scores
    article_with_highest_votes = posts[articles_upvote_scores.index(article_score)]
    # getting the article title and link of the 3 top articles
    for title, link in article_with_highest_votes.items():
        print(f"\n top 3 articles with the highest upvote count:\n Title:{title}\nlink: {link}\n")
