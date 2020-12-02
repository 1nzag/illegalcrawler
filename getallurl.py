import sys
import io
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')    

urlList = []

def request_with_fake_headers(url: str, referer="https://www.google.com"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
        "referer": referer,
    }
    res = requests.get(url, headers=headers, timeout = 5)
    return res

def FilterOtherUrls(urlList, MotherUrl):
    www = ["https://www", "http://www", "www"]
    trash =["twitter.com", "kakao.com", "naver.com"]
    MotherDomain = urlparse(MotherUrl).netloc
    trash.append(MotherDomain)
   
    urlList2 = []
    for url in urlList:
        cnt = 0
        if url.split('.')[0] in www and url.split('.')[1] == MotherUrl.split('.')[1]:
            pass
        elif url.split('.')[0] not in www and url.split('.')[0] == MotherUrl.split('.')[0]:
            pass
        else:
            for t in trash:
                if t == urlparse(url).netloc:
                    cnt += 1
            if cnt == 0:
                urlList2.append(urlparse(url).scheme + "://" + urlparse(url).netloc)
        
    urlSet = set(urlList2)
    urlList2 = list(urlSet)    
    
    return urlList2

def GetTargetUrls(url):
    HTMLtext = request_with_fake_headers(url).text
    soup = BeautifulSoup(HTMLtext, 'html.parser')
    hrefList = soup.find_all('a', href=True)

    for href in hrefList:
        if str(href['href']).startswith("http"):
            urlList.append(str(href['href']))
        
    return FilterOtherUrls(urlList, url)

if __name__ == '__main__':
    GetTargetUrls(sys.argv[1])
