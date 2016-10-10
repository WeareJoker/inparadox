import csv
import mechanize
import urllib2
from bs4 import BeautifulSoup


#Start to input values into csv files
def csvstart(daily):
	csv_file = open("./result/" + str(daily) + "/result.csv",'wb')
	cw = csv.writer(csv_file, delimiter=',',quotechar='|')
	cw.writerow([u"번호".encode("euc-kr"),"name","email","Subject","Receive Time"])
	#Write first line(title line)
	return cw

url = 'https://mail.naver.com'
data = urllib2.urlopen(url) #URL을 새로운 브라우저 창에서 오픈합니다.
html = data.read() #HTML 소스를 읽습니다.
print html.prettify() #prettify 메소드를 통해 조금 더 구분된 html 소스를 출력합니다.

soup = BeautifulSoup(html, "lxml") # lxml parser가 기본 parser보다 더 좋은 성능을 갖고 있습니다.
#SenderName
Fomat1 = </span>(\w+)</strong> #</span>과 </strong>사이 값 출력
for SenderNames in soup.find_all('a',u"보낸 이".encode("euc-kr")):
	print SenderNames #Format을 이용하여 출력하고 싶다()
    ####print SenderName.decode('utf8')
#Subject
Fomat2 = ";(.+?)";  #";"과 ";사이 값 출력
for Subjects in soup.find('a',u"메일 제목:".encode("euc-kr")):
	print Subjects #Format을 이용하여 출력하고 싶다()
	####print Subject.decode('utf8')


'''무시무시
for title in titles:
	print('title:{0:10s} link:{1:20s}\n'.format(title['title'], title['href']))
'''