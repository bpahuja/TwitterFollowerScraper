from bs4 import BeautifulSoup
import requests
import urllib
import random
username = input("Enter Twitter Username : ")

link = f'https://twitter.com/{username}'

HEADERS_LIST = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13",
                "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
                "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
                "Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre"]

HEADER = {'User-Agent': random.choice(HEADERS_LIST)}

response = requests.get(link,headers=HEADER)
html = response.text

r = urllib.request.urlopen(link)
data = r.read()

soup = BeautifulSoup(html,'html.parser')
alist = soup.find_all('a','ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor')
for tag in alist:
    if tag['data-nav'] == 'followers':
        print(tag['title']) 