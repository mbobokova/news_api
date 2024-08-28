import requests
import send_email

topic = "tesla"

api_key = "380784bcf2a5470ab73588032b3dd772"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=380784bcf2a5470ab73588032b3dd772&" \
      "language=en"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
articles = []

for article in content["articles"][0:5]:
    article_str = f"""\
    Author: {article["author"]}
    Title: {article["title"]}
    Description: {article["description"]}
    Read more: {article["url"]}
    """
    articles.append(article_str)

articles_content = "\n\n".join(articles)

message = f"""\
Subject: News from api     
    
Content: {articles_content}
"""

message = message.encode("utf-8")


send_email.send_email(message)



