from html.parser import HTMLParser #html on suur moodul ja parser on selle alamosa
from urllib.request import urlopen
from urllib import parse

class LinkParser (HTMLParser):
    #otsime linke lehelt. Kontrollime
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            if (key,value) in attrs:
                if key == "href":
                    newUrl = parse.urljoin(self.baseUrl,value)
                    self.links=self.links+[newUrl]

    def getLinks(self,url):
        self.links=[]
        self.baseUrl = url
        response = urlopen(url)
        print (response.read())
        #if response.getheader('Content-Type') == 'text/html; charset=utf-8':
        if response.getheader("Content-type") == "text/html":
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString,self.links
        else:
            return "",[]
    def spider(url,word,maxPages):#objekt klassi sees
        pagesToVisit =[url]
        numberVisited = 0
        foundWord = False
        #while numberVisited < maxPages and pagesToVisit != []:
        while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
            numberVisited = numberVisited+1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numberVisited,"Visiting", url)
                data,links = LinkParser.getLinks(url)
                if data.find(word)>-1:
                    foundWord = True
                pagesToVisit = pagesToVisit + links
                print ("Õnnestus!")
            except:
                print ("Halvasti läks")
        if foundWord:
            print ("Sõna",word," leidsie aadressilt ", url)
        else:
            print ("Sellist sõna ei leidnud")