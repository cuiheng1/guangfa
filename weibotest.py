# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib
import random

class ScrapyPages:

    #网页内容保存目录
    contentDir = "D:\\pages\\"
    #网页链接保存目录
    atagsDir = "D:\\atags\\"
    #保存网页与文件名对应关系的文件
    mappingFile = "D:\\mapping"
    #已处理的链接
    handledLinks = []
    #待处理的链接
    unhandledLinks = []





    #这个过程也要改动
    #保存页面内容(仅文字)
    def savePageContent(self, filename, content):
        tfile= open(self.contentDir + filename,'wb')
        tfile.write(content)
        print('writing file-',filename)
        tfile.close()
    


   


    #爬取网页的入口函数
    def scrapy(self, initURL):
        self.unhandledLinks += [initURL]
        while len(self.unhandledLinks) != 0:
            #随机访问未访问的链接？
            pos = random.randint(0,len(self.unhandledLinks) - 1)
            print('-pos-',pos)
            link = self.unhandledLinks[pos]
            del self.unhandledLinks[pos]
            driver = self.openPage(link)
            content = str(driver.find_element_by_xpath(".//html").text.encode('utf-8'))
            if len(content) > 512:   
                atags = driver.find_elements_by_tag_name("a")
                filename = self.urlToFilename(link)
                self.handleAnchor(filename, atags)
                self.savePageContent(filename,link + '\n' + content)
            driver.close()
            
        
pageScrapy = ScrapyPages()
pageScrapy.scrapy('http://news.baidu.com/ns?word=%B1%BB%B5%F7%B2%E9&tn=news&from=news&cl=2&rn=20&ct=1')