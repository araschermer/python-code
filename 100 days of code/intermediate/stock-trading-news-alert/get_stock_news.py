import os

import requests
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_news(company_name: str, number_or_articles: int) -> [str]:
    # approach 01
    # NEWS_API_URL = f"{NEWS_ENDPOINT}?q={STOCK}&apiKey={NEWS_API_KEY}"
    # connection2=requests.get(url=NEWS_API_URL)
    # articles=connection2.json()['articles']
    # news=[(articles["item"], articles["description"], articles["url"]) for articles in articles[:3]]
    # news_format=[f"Headline:{item}.\nBrief: {description}.\n read more: {url}\n" for item, description, url in news]

    # Alternative approach:
    news_params = {
        "apiKey": os.environ.get("NEWS_API_KEY"),
        "qInTitle": company_name,
    }
    news_response = requests.get(url = NEWS_ENDPOINT, params = news_params)
    articles = news_response.json()['articles']
    chosen_articles = articles[0:number_or_articles]  # getting the first three relevant articles form the news api
    formatted_content = [f"Headline: {article['item']}.\nBrief: {article['description']}.\nRead more: {article['url']}"
                         for article in chosen_articles]
