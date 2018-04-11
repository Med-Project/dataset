import time, requests, codecs ,json
from bs4 import BeautifulSoup
from lxml import html
import pandas

s = requests.Session()

ref = codecs.open('mailru/ref_for_mailru.txt',"w",'utf-8')
file = codecs.open('mailru/text.txt',"w",'utf-8')

url ='https://otvet.mail.ru/health_beauty/'
# cur =0
# while True:
# 	if cur > 385:
# 		break
# 	url = "https://diseases.medelement.com/?searched_data=diseases&q=&mq=&tq=&diseases_filter_type=list&diseases_content_type=2&section_medicine=0&category_mkb=0&parent_category_mkb=0&skip=" + str(cur)
		  
# 	page =  s.get(url)
	
# 	print(page.status_code, cur)

# 	if page.status_code == 200:
# 		soup = BeautifulSoup(page.content, 'lxml')
# 		mu = soup.find("div",{"class":"pageQuestions"})

		
# 		for i in mu:
# 			ur = "https://diseases.medelement.com" + i['href']
# 			ref.write(str(ur)+ "\n")
# 			page =  s.get(ur)
# 			soup = BeautifulSoup(page.content, 'lxml')
# 			main = soup.find("main",{"id":"main"})
# 			su = main.find_all("section")
# 			for j in range(1,len(su)-2):
# 				words = su[j].text.strip() 
# 				# words = re.sub("[0-9]+[\.]","", words)
# 				file.write(words+"\n")
# 			#[A-Za-zа-яА-Я]

# 	cur += 10
