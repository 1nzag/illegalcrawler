from tree import Node
from tree import Tree
from getallurl import *
from isilegal import *
import sys




def run(RootURL):
    depthcount = 0
    URLTreeRoot = Tree(Node(RootURL))
    URLList = GetTargetUrls(RootURL)
    
    #print(URLList)
    FilteredURLList = []
    for URL in URLList:
        if IsIllegalURL(URL) == True:
            FilteredURLList.append(URL)
            open("crawled.txt", "a").write("%s\n" % URL)
            print("%s" % URL, flush = True)
    
    for URL in FilteredURLList:
        URLTreeRoot.root.Insert(Node(URL))

    while True:
        print("[*] depth: %d" % depthcount, flush = True)
        URLNodeList = URLTreeRoot.FindDepthNode(depthcount)
        if len(URLNodeList) == 0:
            print("[!] no more URL", flush = True)
            break
        
        nodecnt = 0
        for URLNode in URLNodeList:
            URLList = GetTargetUrls(URLNode.data)
            FilteredURLList = []
            #print(URLList)
            print("[*]node count: %d" % nodecnt, flush = True)
            for URL in URLList:
                if IsIllegalURL(URL) == True and URLTreeRoot.FindItem(URL) == False:
                    FilteredURLList.append(URL)
                    open("crawled.txt", "a").write("%s\n" % URL)
                    print("%s" % URL, flush = True)

            
            for URL in FilteredURLList:
                URLNode.Insert(Node(URL))
            nodecnt += 1
            
        depthcount += 1
    
    exit()



if __name__ == '__main__':
    run("https://manapang1.com/")