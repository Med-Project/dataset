import time, requests, codecs ,json , re
from bs4 import BeautifulSoup
from lxml import html
import pandas
s = requests.Session()

comman = codecs.open('medpoisk/text.txt',"w",'utf-8')
ref = codecs.open('medpoisk/reference_for_bolezn.txt',"w",'utf-8')

num = 0
for i in range(1,19):
	url = 'https://www.medpoisk.ru/bolezni/page_'+  str(i)+'.html'
	page =  s.get(url)
	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'lxml')
		mu = soup.find_all("div",{"class":"row sites_list_row"})
		for i in mu:
			ur = i.find('a')['href']
			ref.write(ur + "\n")
			page =  s.get(ur)
			soup = BeautifulSoup(page.content, 'lxml')
			# h1 = soup.find("h1").text
			su = soup.find("div",{"class":"row med_flexbox"})
			words = su.text.strip() 
			# words = re.sub("[0-9]+[\.]","", words)
			#[A-Za-zа-яА-Я]
			comman.write(words+"\n")
			file = codecs.open('medpoisk/htmls/'+ str(num)+'.txt',"w",'utf-8')
			file.write( str(su) )
			file.close()
			num += 1
			# break
	else:
		print(i,page.status_code)
	# print(i)
	# break



