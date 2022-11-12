import fonctions
import requests
import re

url="http://books.toscrape.com/"
urlCata="http://books.toscrape.com/catalogue/"

reponse=fonctions.fonctionGetContent(url)
soup=fonctions.createObjectSoup(reponse)

tabUrls=fonctions.fonctionGetUrlsOfAllPages(soup,urlCata)

urlImages=fonctions.getAllUrlsImg(tabUrls)

urlFormater=[]
#formatage
for  urlpic in urlImages:
      newLink=re.sub("../","https://books.toscrape.com/",urlpic,1)
      urlFormater.append(newLink)

fonctions.downloadImages(urlFormater)