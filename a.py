# coding=utf-8
import sys
import requests
from bs4 import BeautifulSoup

#usage
print '\nUsage: python a.py\n'
print 'Example for searching personal data:'
print 'Choose search engine(Google = 1, Baidu = 2, Bing = 3): 1'
print 'site:.gov.tw intitle:"index of" inurl:"index" ext:xls | "身分證" | "電話" | "名單"...\n'
print 'If there is no any response while using Google Search engine, change search engine, please.'
print 'Ctrl + c to interrupt.\n\n'
print 'Output.txt will generate at current directory.'
print 'Created by KPMG Cyber Security and Crime Lab 2017.5.'

choose_engine = raw_input("\nChoose search engine: ")
site = raw_input("site: ")

#headers setting
headers = {#'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +Googlebot - Webmaster Tools Help)',  
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
      'Connection':'Keep-Alive',
      'Accept-Language':'zh-CN,zh;q=0.8',
      'Accept-Encoding':'gzip,deflate,sdch',
      'Accept':'*/*',
      'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
      'Cache-Control':'max-age=0'
      }  

count = 1 #item record 
start = 0 #searching engine web page
stop = 0

with open(r'Output.txt','w') as f:
    while( True ):  
        if(choose_engine == '1'): #google engine
            print "Google Search"
            url = "https://www.google.com.tw/search?q="
            url += "site:"
            url += site
            url += "&start="
            url += str(start)
            #url += "&tbs=qdr:" # y=yaer, m=month, d=day, h=hour  #you can change searching time
            #url +="&gs_l=serp.3...1488510.1488510.0.1489227.1.1.0.0.0.0.0.0..0.0....0...1c.2.64.serp..1.0.0.huEsFQ86mZQ" #
        
        elif(choose_engine == '2'): #baidu engine
            print "Baidu"
            url = "http://www.baidu.com/s?ie=utf-8tn=baidu&wd="
            url += "site:"
            url += site
            url += "&pn="
            url += str(start)
        
        elif(choose_engine == '3'): #bing engine
            print "Bing"
            url = "https://www.bing.com/search?q="
            url += "site:"
            url += site
            url += "&first="
            url += str(start)
        
        try:
            res = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            r.status_code = "\n"
        soup = BeautifulSoup(res.text, "html.parser")

        #for google
        if(choose_engine == '1'):
            page_str = "=======[Page: {start} ]=======\n{url}\n".format(start=start+1, url=url)
            f.write(page_str)
            print page_str
            if soup.select(".r"):
                for title in soup.select(".r"):
                    #print title.text
                    #print title.find('a')['href']
                    title_str = ("=======[ {count} ]=======\n"+\
                                "{title_text} \n"+\
                                "{title_href} \n")\
                                .format(count=count,
                                    title_text=title.text.encode('utf-8'),
                                    title_href=title.find('a')['href'])
                    f.write(title_str)
                    print title_str
                    count += 1
            #if google not found
            else:
                print '=======[Page Not Found ]=======\n','Finish.\n'
                Finish_str = ("=======[Page Not Found ]=======\nFinish.\n")
                f.write(Finish_str)
                break
            start += 1
                         
        #for baidu
        elif(choose_engine == '2'):
            page_str = "=======[Page: {start} ]=======\n{url}\n".format(start=(start+10)/10, url=url)
            f.write(page_str)
            print page_str
            if soup.select(".t"):
                for title in soup.select(".t"):
                    #print title.text
                    #print title.find('a')['href']
                    title_str = ("=======[ {count} ]=======\n"+\
                                "{title_text} \n"+\
                                "{title_href} \n")\
                                .format(count=count,
                                    title_text=title.text.encode('utf-8'),
                                    title_href=title.find('a')['href'])
                    f.write(title_str)
                    print title_str
                    count += 1
            #if baidu not found
            else:
                print '=======[Page Not Found ]=======\n','Finish.\n'
                Finish_str = ("=======[Page Not Found ]=======\nFinish.\n")
                f.write(Finish_str)
                break
            start += 1

        #for bing
        elif(choose_engine == '3'):
            page_str = "=======[Page: {start} ]=======\n{url}\n".format(start=(start+10)/10, url=url)
            f.write(page_str)
            print page_str
            if soup.select(".b_algo"):
                for title in soup.select(".b_algo"):
                    #print title.text
                    #print title.find('a')['href']
                    title_str = ("=======[ {count} ]=======\n"+\
                            "{title_text} \n"+\
                            "{title_href} \n")\
                            .format(count=count,
                                title_text=title.text.encode('utf-8'),
                                title_href=title.find('a')['href'])
                    f.write(title_str)
                    print title_str
                    count += 1
            #bing if not found
            else:
                print '=======[Page Not Found ]=======\n','Finish.\n'
                Finish_str = ("=======[Page Not Found ]=======\nFinish.\n")
                f.write(Finish_str)
                break
            start += 1

