import requests
import send_email

api_key = "380784bcf2a5470ab73588032b3dd772"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-26&sort" \
    "By=publishedAt&apiKey=380784bcf2a5470ab73588032b3dd772"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
articles = []

for article in content["articles"][0:5]:
    articles_str = f"""\
    Author: {article["author"]}
    Title: {article["title"]}
    Description:{article["description"]}
    """
    articles.append(articles_str)

articles_content = "\n\n".join(articles)

message = f"""\
Subject: News from api 
    
    
Content: {articles_content}
"""

message = message.encode("utf-8")


send_email.send_email(message)



