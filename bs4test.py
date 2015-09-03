#
# -*- coding: utf-8 -*-

#---------------------------------import---------------------------------------
import urllib2;
import re;
from bs4 import BeautifulSoup;

#------------------------------------------------------------------------------
def main():
    userMainUrl = "http://news.baidu.com/ns?ct=1&rn=20&ie=utf-8&bs=%E8%A2%AB%E8%B0%83%E6%9F%A5&rsv_bp=1&sr=0&cl=2&f=8&prevct=no&tn=news&word=%E4%BC%81%E4%B8%9A%E8%A2%AB%E8%B0%83%E6%9F%A5&rsv_sug3=4&rsv_sug4=278&rsv_sug1=1&rsv_sug2=0&inputT=964&rsv_sug=1";
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    #print "respHtml=",respHtml; # you should see the ouput html

 
    print "Method 2: Use python third lib BeautifulSoup to extract info from html";
    songtasteHtmlEncoding = "GB2312";
    soup = BeautifulSoup(respHtml, from_encoding=songtasteHtmlEncoding);
    #<h1 class="h1user">crifan</h1>
    foundClassBold = soup.find(attrs={"class":"c-title"});
    print "foundClassBold=%s",foundClassBold;
    if(foundClassBold):
        BoldStr = foundClassBold.string;
        print "标题=", BoldStr;

###############################################################################
if __name__=="__main__":
    main(); 