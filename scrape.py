import urllib.request as urllib
from urllib.request import urlopen
import requests
import bs4 as bs
import re
proxy = []
def write():
    global proxy
    print(len(proxy))
    infile = open('proxylist.txt','r')
    ip = infile.readlines()
    newFile = open('proxylist.txt','a')
    check = False
    for x in range(int(len(proxy))):
        for line in (ip):
            if (proxy[x] in line):
                print("Duplicate ip")
                check = True
                break
        if(not check):
            newFile.write(proxy[x]+"\n")
            print("WRITE"+str(x))
        check = False

def proxynova():
    global proxy
    proxy = []
    url = "https://www.proxynova.com/proxy-server-list/country-th/" 
    html = urllib.urlopen(url).read()
    soup = bs.BeautifulSoup(html,'lxml')
    table = soup.find('table',id='tbl_proxy_list')
    rows = table.find_all('tr')
    #for row in rows:
        #labels.append(str(row.find_all('td')[0].text))
        #data.append(str(row.find_all('td')[1].text))
    picID=""
    #print(rows)
    if "document.write"in str(rows):
        for line in str(rows).splitlines():
            #print(line)
            line = line.replace(' ','')
            if("document.write" in line):
                line = line.replace('(','x')
                line = line.replace(')','x')
                line = line.replace('\'','')
                #print(line)
                m = re.search("document.writex(.+)x;",line)
                if m:
                    proxID = m.group(1)
            e = re.search('(^[0-9]+)',line)
            if(e):
                proxy.append(str(proxID)+":"+str(e.group(1)))
def spyone():
    global proxy
    proxy = []
    url = "http://spys.one/free-proxy-list/TH/" 
    #html = urllib.urlopen(url).read()
    html = requests.get(url)
    soup = bs.BeautifulSoup(html.text,'lxml')
    table = soup.find('table',cellspacing='0')
    rows = table.find_all('tr')
    #for row in rows:
        #labels.append(str(row.find_all('td')[0].text))
        #data.append(str(row.find_all('td')[1].text))
    picID=""
    rows = str(rows).split(" ago)")
    #print(rows[0])
    #print(len(rows))
    for i in range(len(rows)):
        rows[i] = str(rows[i]).replace('<font class="spy14">','thisip')
        rows[i] = str(rows[i]).replace('<script type="text/javascript">','thisip')
        m = re.search('thisip(.+?)thisip',str(rows[i]))
        if m: 
            if(not "Next" in m.group(1)):
                proxID = m.group(1)
                print(proxID)
                proxy.append(str(proxID)+":8080")
    #print(proxy)

spyone()  
write()
proxynova()
write()
        
