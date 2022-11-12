import requests
import re

from bs4 import  BeautifulSoup

# Generation du contenu de la page
def fonctionGetContent(url):
    reponse=requests.get(url)
    if(reponse.status_code!=200):
        print(" Erorr chargement de page")
    else:
        content=reponse.content
    return content


# Creation de l'objet soup
def createObjectSoup(content):
    soup=BeautifulSoup(content,"html.parser")
    if(soup):
        return soup
    else:
        print("Erorr creation objet")

# Extraction des entiers depuis une chaine de caractere
def getIntegersFromString(string):
    returnvalue = []
    for x in string.split():
        try:
            returnvalue.append(int(x))
        except:
            pass
    return returnvalue

 # Recuperation du nombre Max des pages
def getNumberMaxOfPages(value):
    return value[-1]

# recuperation des liens de toutes les pages
def getAllPagesLinks(nbMax,urlhome):
    numberPage=1
    numberPageMax=nbMax
    urlInfos=[]
    for numberPage in range(1,numberPageMax+1):
        try:
            url="page-"+str(numberPage)+".html"
            urlInfos.append(urlhome+url)
        except:
            print("error: chargement de la page")
    return urlInfos

# Extraction de toutes les urls des pages toutes confondues        
def fonctionGetUrlsOfAllPages(soup,url):
    tabLinks=[]
    current=soup.find('section').find("ul",class_='pager').find("li",class_="current")  
    valueCurrent=getIntegersFromString(current.string)
    nbMax=getNumberMaxOfPages(valueCurrent)
    tabLinks=getAllPagesLinks(nbMax,url)
    return tabLinks

#Extraction des urls des images
def getAllUrlsImg(tabLinks):
    imagesUrls=[]
    for link in tabLinks:
        reponse=requests.get(link)
        soup=createObjectSoup(reponse.content)
        images=soup.findAll("img")
        for img in images:
            imagesUrls.append(img["src"])

        # ajout des informations dans un tableau
    
    return imagesUrls

# Telechargement des images
def downloadImages(listUrlImages):
    number=0
    for imgUrl in listUrlImages:
        with open("Images\images"+str(number)+".jpg","wb")as f:
            response = requests.get(imgUrl)
            f.write(response.content)
        number=number+1
    print("download successful")