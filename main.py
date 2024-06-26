import requests

api_key = "380784bcf2a5470ab73588032b3dd772"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-26&sort" \
    "By=publishedAt&apiKey=380784bcf2a5470ab73588032b3dd772"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["author"])