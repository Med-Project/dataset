import requests
import re
import os
import json
import codecs
import pandas as pd

mainUrl = 'https://www.medikforum.ru/forum/'

page = requests.get(mainUrl)

urlReg = r'(?<=a href=")(.*)(?=" class="forumtitle")'
forumNameReg = r'(?<=<div id="pageheader">\n<h1>)(.*)(?=</h1>)'
topicReg = r'(?<=href=")(.*)(?=" class="topictitle")'
topicNameReg = forumNameReg 
commentReg =  r'(?<=<p>)(.*)(?=</p>\n<div class="mass">)'
arr = re.findall(urlReg, page.text)
nextReg = r'(?<=<li class="next veil reveal-md-inline"><a href=")(.*)(?="><span>)'

def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)

def parseTopic(url):
    allCommnets = []

    while True:
        commnetsPage = requests.get(url)
        comments = re.findall(commentReg, commnetsPage.text) 
        allCommnets = allCommnets + comments
        nextUrl = re.findall(nextReg, commnetsPage.text)
        if(len(nextUrl) == 0):
            break
        url = nextUrl[0]

    tName = re.findall(topicNameReg, commnetsPage.text)    
    return tName[0], allCommnets

def parseForum(url):
    content = requests.get(url)
    forumName = re.findall(forumNameReg, content.text)[0]

    forumName = re.sub('[^\w]', ' ', forumName)
    forumName = '_'.join([i for i in forumName.split(' ')])

    createFolder(forumName)
    
    num = 0
    while True:
        topics = re.findall(topicReg, content.text)
        for t in topics:
            tName, comments = parseTopic(t) # tName name of topic, comments json 
            
            with codecs.open(forumName + '/' + str(num)+'.txt', "w+", "utf-8")  as f:
                json.dump(comments, f, ensure_ascii=False)
            num += 1
        
        nextUrl = re.findall(nextReg, content.text)
        if(len(nextUrl) == 0):
            break
        url = nextUrl[0]
        content = requests.get(url)


for url in arr:
    parseForum(url)