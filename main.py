import requests
from datetime import datetime, timedelta

query = input("What type of news are you interested in today? ")

api = "dbe57b028aeb41e285a226a94865f7a7"

yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

url = f"https://newsapi.org/v2/everything?q={query}&from={yesterday}&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data = r.json()

if data.get("status") != "ok":
    print("Error:", data.get("message"))
else:
    articles = data.get("articles", [])
    if not articles:
        print("No articles found for this query.")
    else:
        for index, article in enumerate(articles):
            print(index + 1, article["title"])
            print(article["url"])
            print("\n****************************************\n")
