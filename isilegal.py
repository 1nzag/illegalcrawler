import requests
from bs4 import BeautifulSoup

titleList = ["웹툰", "만화", "성인", "망가", "소설", "야동", "애니", "에니"]

def request_with_fake_headers(url: str, referer="https://www.google.com"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
        "referer": referer,
    }
    return requests.get(url, headers=headers, timeout = 5)

def IsImport(textlist, deststring):
    for text in textlist:
        if text in deststring:
            return 1
    return 0

def ValidateMetadata(metadataList):
    result = 0
    for metadata in metadataList:
        result += IsImport(titleList, str(metadata))

    return result

def CalcGifnum(imgtagList):
    result = 0
    for imgtag in imgtagList:
        if '.gif' in str(imgtag):
            result += 1
    return result

def IsIllegalURL(URL):
    score = 0
    try:
        HTMLtext = request_with_fake_headers(URL).text
    except:
        return False
    soup = BeautifulSoup(HTMLtext, 'html.parser')

    #title score
    try:
        Title = str(soup.find_all('title')[0])
        score += IsImport(titleList, Title) * 500
    except:
        pass
    score += ValidateMetadata(soup.find_all('meta')) * 300
    #banner score
    score += CalcGifnum(soup.find_all('img'))
    
    if score >= 1200:
        return True
    else:
        return False


if __name__ == '__main__':
    #URLlist = open("URLlist.txt", "r").read()
    #for url in URLlist.split("\n"):
    #    print("%s: %d" % (url, IsIllegalURL(url)))
    print(IsIllegalURL("https://newtoki73.net"))