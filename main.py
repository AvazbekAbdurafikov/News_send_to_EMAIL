import requests
from sent_eamil import send_mail
url = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2024-04-09&sortBy=publishedAt&apiKey=f07773d8e3"
       "c74e0e8eb3f4c475906bc6")

api = "f07773d8e3c74e0e8eb3f4c475906bc6"
response = requests.get(url)
news = ""
data = response.json()
for i in data['articles']:
    if i["title"] is not None:
        news = f"{news} \n {i['title']} \n {i['description']} + \n\n "

news = news.encode("utf-8")
send_mail(message=news)
