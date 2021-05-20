import requests
from bs4 import BeautifulSoup

url = "https://www.gachon.ac.kr/community/opencampus/03.jsp?boardType_seq=358"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

ranks = soup.find_all("td", attrs = {"class":"tl"})

for rank in ranks:
    title = rank.a.get_text()
    link = rank.a["href"]

import telegram
토큰 = "1835518048:AAFzzz7WNfrdGD1bG8sHdl5sE4fltlK3LUE"
봇 = telegram.Bot(token=토큰)

#id 알아보기
# for i in 봇.getUpdates():
#     print(i.message)

봇.send_message(1895249171,title)