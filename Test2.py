# -*- coding:utf-8 -*-
import csv
import urllib3
import requests
from bs4 import BeautifulSoup
import sqlite3

url = "http://www.naver.com"
html = urllib3.connection_from_url(url)
html_data = html.urlopen('GET',url)
#print(html_data.data)
#quit()
soup = BeautifulSoup(html_data, "lxml")

#Subject 메일 제목 저장
Subject_list = []
for Subjects in soup.find_all('strong'):
	Subject_list.append(Subjects.next_sibling)
	print(Subjects.text, Subjects.next_sibling)

#SenderName 보낸 이 저장
SenderName_list = []
Senders = soup.find_all("div", "mTitle")
Send = [div.a["title"] for div in Senders]
for Seg in Send:
	SenderName_list.append(Seg)
	print (Seg)

DB = dict()
for SN in SenderName_list:
	i=0
	if SN != NULL:
		DB = {SN:Subject_list[i]}
		i+=1
	else:
		break