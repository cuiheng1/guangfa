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



    def openPage(self, url):
        driver = webdriver.Firefox() 
        driver.get(url)
        return driver

    #根据url获得文件名
    def urlToFilename(self, url):
        m = hashlib.sha256()
        m.update(url.encode('utf-8'))
        filename = m.hexdigest()
        tfile = open(self.mappingFile, 'wb+')
        tfile.write(filename + ', ' + url + '\n')
        return filename
    #这个过程也要改动
    #保存页面内容(仅文字)
    def savePageContent(self, filename, content):
        tfile= open(self.contentDir + filename,'wb')
        tfile.write(content)
        print('writing file-',filename)
        tfile.close()
    
    #处理页面中的a标签：
    #1、将a标签存入相应的文件中
    #2、将其更新如links中        
    def handleAnchor(self, filename, anchors):
        hrefs = self.extractHrefFromAnchor(anchors)
        self.addHrefsToLinks(hrefs)
        self.saveAnchor(filename, hrefs)

    #将新提取到的链接（未出现过的）加入待处理链接中
    def addHrefsToLinks(self, hrefs):
        for href in hrefs:
            if href in self.handledLinks or href in self.unhandledLinks:
                continue
            else:
                self.unhandledLinks += [href]
    #保存页面链接
    def saveAnchor(self, filename, hrefs):
        afile= open(self.atagsDir + filename,'wb')
        afile.write('\n'.join(hrefs))
        afile.close()
   
    #从a标签中提取链接 并判断链接
    def extractHrefFromAnchor(self, anchors):
        hrefs = []
        for anchor in anchors:
            try:
                href = anchor.get_attribute('href').encode('utf-8')
                if href.find('http://news.baidu.com') == -1 or href in hrefs:
                    continue
                else:
                    hrefs += [href]
            except AttributeError:
                pass
            except selenium.common.exceptions.StaleElementReferenceException:
                pass
        return hrefs

    #爬取网页的入口函数
    def scrapy(self, initURL):
        driver = webdriver.Firefox()
        self.unhandledLinks += [initURL]
        while len(self.unhandledLinks) != 0:
            #随机访问未访问的链接？
            pos = random.randint(0,len(self.unhandledLinks) - 1)
            print('-pos-',pos)
            link = self.unhandledLinks[pos]
            del self.unhandledLinks[pos]
            driver.get(link)
            content = str(driver.find_element_by_xpath(".//html").text.encode('utf-8'))
            if len(content) > 512:   
                atags = driver.find_elements_by_tag_name("a")
                filename = self.urlToFilename(link)
                self.handleAnchor(filename, atags)
                self.savePageContent(filename,link + '\n' + content)
            driver.close()
            
        
pageScrapy = ScrapyPages()
pageScrapy.scrapy('http://news.baidu.com/ns?word=%B1%BB%B5%F7%B2%E9&tn=news&from=news&cl=2&rn=20&ct=1')