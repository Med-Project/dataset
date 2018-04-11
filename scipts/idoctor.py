import time, requests, codecs ,json , re
from bs4 import BeautifulSoup
from lxml import html
import pandas
s = requests.Session()

comman = codecs.open('idoctor/text.txt',"w",'utf-8')
ref = codecs.open('idoctor/reference_for_news.txt',"w",'utf-8')

num=0
for i in range(1,22):
	url = 'https://idoctor.kz/posts?page=' + str(i)
	page =  s.get(url)
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'lxml')
		mu = soup.find_all("div",{"class":"news__item item-news"})
		for i in mu:
			ur = i.find('a')['href']
			ref.write(ur + "\n")
			page =  s.get(ur)
			soup = BeautifulSoup(page.content, 'lxml')
			h1 = soup.find("h1").text
			su = soup.find("div",{"class":"middle"})
			words = su.text.strip() 
			# words = re.sub("[0-9]+[\.]","", words)
			#[A-Za-zа-яА-Я]
			comman.write(words+"\n")
			file = codecs.open('idoctor/htmls/'+ str(num)+'.txt',"w",'utf-8')
			file.write( str(su) )
			file.close()
			num += 1
	else:
		print(i,page.status_code)

	# break



