import requests
from sent_eamil import send_mail

topic = "tesla"
language = "ru"
url = (f"https://newsapi.org/v2/everything?q={topic}&"
       f"from=2024-04-09&"
       f"sortBy=publishedAt&"
       f"apiKey=f07773d8e3c74e0e8eb3f4c475906bc6&"
       f"language={language}")

api = "f07773d8e3c74e0e8eb3f4c475906bc6"
response = requests.get(url)
news = ""
data = response.json()
for i in data['articles'][:20]:
    if i["title"] and i["description"] is not None:
        news = ("Subject:Today`s news" + "\n" + news + i['title'] + "\n" + "\n" + i['description'] + "\n" + i["url"] +
                 2*"\n")

news = news.encode("utf-8")
send_mail(message=news)
