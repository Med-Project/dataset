import time, requests, codecs ,json
from bs4 import BeautifulSoup
from lxml import html
import pandas

s = requests.Session()

def mat():
	ref = codecs.open('medelement/ref_for_medel_zabolev.txt',"w",'utf-8')
	file = codecs.open('medelement/text.txt',"w",'utf-8')

	cur =0
	while True:
		if cur > 385:
			break
		url = "https://diseases.medelement.com/?searched_data=diseases&q=&mq=&tq=&diseases_filter_type=list&diseases_content_type=2&section_medicine=0&category_mkb=0&parent_category_mkb=0&skip=" + str(cur)
			  
		page =  s.get(url)

		print(page.status_code, cur)

		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'lxml')
			mu = soup.find_all("a",{"class":"results-item__title-link"})
			for i in mu:
				ur = "https://diseases.medelement.com" + i['href']
				ref.write(str(ur)+ "\n")
				page =  s.get(ur)
				soup = BeautifulSoup(page.content, 'lxml')
				main = soup.find("main",{"id":"main"})
				su = main.find_all("section")
				for j in range(1,len(su)-2):
					words = su[j].text.strip() 
					# words = re.sub("[0-9]+[\.]","", words)
					file.write(words+"\n")
				#[A-Za-zа-яА-Я]

		cur += 10



def obzor_stati():
	cur = 0
	num = 0
	while True:
		if cur > 385:
			break
		url = "https://diseases.medelement.com/?searched_data=diseases&q=&mq=&tq=&diseases_filter_type=list&diseases_content_type=2&section_medicine=0&category_mkb=0&parent_category_mkb=0&skip=" + str(cur)
			  
		page =  s.get(url)
		
		print(page.status_code, cur)

		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'lxml')
			mu = soup.find_all("a",{"class":"results-item__title-link"})
			for i in mu:
				ur = "https://diseases.medelement.com" + i['href']
				page =  s.get(ur)
				soup = BeautifulSoup(page.content, 'lxml')
				main = soup.find("main",{"id":"main"})
				file = codecs.open('medelement/'+ str(num)+'.txt',"w",'utf-8')
				file.write( str(main) )
				file.close()
				num += 1

				
		cur += 10


def clin_rf():
	cur = 0
	num = 0
	while True:
		if cur > 213:
			break
		url = "https://diseases.medelement.com/?searched_data=diseases&diseases_filter_type=list&diseases_content_type=270857091501043305&skip=" + str(cur)
			  
		page =  s.get(url)
		
		print(page.status_code, cur)

		if page.status_code == 200:
			soup = BeautifulSoup(page.content, 'lxml')
			mu = soup.find_all("a",{"class":"results-item__title-link"})
			for i in mu:
				ur = "https://diseases.medelement.com" + i['href']
				page =  s.get(ur)
				soup = BeautifulSoup(page.content, 'lxml')
				main = soup.find("main",{"id":"main"})
				file = codecs.open('medelement_clin_rf/'+ str(num)+'.txt',"w",'utf-8')
				file.write( str(main) )
				file.close()
				num += 1

				
		cur += 10


cur = 0
num = 0
while True:
	if cur > 1994:
		break
	url = "https://diseases.medelement.com/?searched_data=diseases&q=&mq=&tq=&diseases_filter_type=list&diseases_content_type=4&section_medicine=0&category_mkb=0&parent_category_mkb=0&skip=" + str(cur)
	# url ='https://diseases.medelement.com/?searched_data=diseases&q=%D0%B1%D0%BE%D0%BB%D1%8C&mq=&tq=&diseases_filter_type=list&diseases_content_type=4&section_medicine=0&category_mkb=0&parent_category_mkb=0'  
	page =  s.get(url)
	
	print(page.status_code, cur)

	if page.status_code == 200:
		soup = BeautifulSoup(page.content, 'lxml')
		br = soup.find_all("div",{"class":"row results-item"})
		mu = soup.find_all("a",{"class":"results-item__title-link"})
		for i in range (0,len(mu) ):
			ur = "https://diseases.medelement.com" + mu[i]['href']
			tem = br[i].find("div",{"class":"results-item__value results__archive"})
			print(str(num))
			if str(tem)!="None":
				continue
			page =  s.get(ur)
			soup = BeautifulSoup(page.content, 'lxml')
			main = soup.find("main",{"id":"main"})
			file = codecs.open('medelement_clin_prot_rk/'+ str(num)+'.txt',"w",'utf-8')
			file.write( str(main) )
			file.close()
			num += 1

	# break

			
	cur += 10