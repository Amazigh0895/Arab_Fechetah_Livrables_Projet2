import requests
from bs4 import  BeautifulSoup
import re
import csv

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

# Extraction de toutes les urls des categories
def getAllCategoriesLinks(soup,url):
    tabUrlsCategories=[]
    categories=soup.find("div",class_="side_categories").find("ul").find("li").find("ul").findAll("a")
    for category in categories:
        tabUrlsCategories.append(url+category["href"])
    return tabUrlsCategories
# Extraction de toutes les noms des categories
def getAllCategoriesNames(soup):
    tabCategoriesNames=[]
    categories=soup.find("div",class_="side_categories").find("ul").find("li").find("ul").findAll("a")
    for category in categories:
        tabCategoriesNames.append(category.string.split())
    return tabCategoriesNames

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

# Recuperation du nombre Max des pages
def getNumberMaxOfPages(value):
    return value[-1]

# Extraction des entiers depuis une chaine de caractere
def getIntegersFromString(string):
    returnvalue = []
    for x in string.split():
        try:
            returnvalue.append(int(x))
        except:
            pass
    return returnvalue
# recuperation des liens de toutes les pages
def getAllPagesLinks(nbMax,urlhome):
    numberPage=1
    numberPageMax=nbMax
    urlInfos=[]
    for numberPage in range(1,numberPageMax+1):
        try:
            url="http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
            url="http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"
            urlFormat=re.sub("index","page-"+str(numberPage),urlhome)
            urlInfos.append(urlFormat)
        except:
            print("error: chargement de la page")
    return urlInfos

#recuperation des contenus(livres) dans plusieurs pages
def getAllContentsOfPages(tabLinks):
    allContentsOfPages=[]
    for link in tabLinks:
        reponse=requests.get(link)
        soup=createObjectSoup(reponse.content)
        titres=soup.findAll("h3")
        for titre in titres:
            allContentsOfPages.append(titre.find("a")["href"])
    return allContentsOfPages

# Extraction de toutes les urls des pages toutes confondues
def fonctionGetUrlsOfAllPages(soup,url):
    tabLinks=[]
    current=soup.find('section').find("ul",class_='pager').find("li",class_="current")  
    valueCurrent=getIntegersFromString(current.string)
    nbMax=getNumberMaxOfPages(valueCurrent)
    tabLinks=getAllPagesLinks(nbMax,url)
    return tabLinks

#Extraction des contenu des livres
def getContentsOfProducts(tabLinks):
    ContentsOfbooks=[]
    for link in tabLinks:
        reponse=requests.get(link)
        soup=createObjectSoup(reponse.content)
        universal_product_code=soup.findAll('tr')[0].find('td').contents[0]
        title=soup.find("h1").contents[0]
        price_including_tax=soup.findAll('tr')[3].find('td').contents[0]
        price_excluding_tax=soup.findAll('tr')[2].find('td').contents[0]
        number_available=soup.findAll('tr')[5].find('td').contents[0]
        product_description=soup.find("article").findChildren("p")[3].contents[0]
        category=soup.findAll('tr')[1].find('td').contents[0]
        review_rating=soup.findAll('tr')[6].find('td').contents[0]
        image_url=soup.find("img")['src']

        # ajout des informations dans un tableau
        ContentsOfbooks.append([universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url])
    return ContentsOfbooks

# Verification de l'existence de plusieurs pages
def HaveOnePage(value):
    return value

# recuperation des contenus ayant une seule page
def getContentOnOnePage(soup):
    titres=soup.findAll("h3")
    urlInfos=[]
    for titre in titres:
        urlInfos.append(titre.find("a")["href"])
    return urlInfos

# Extraction des contenu selon la categorie
def getContentByCategory(url):

    reponse=fonctionGetContent(url)
    soup=createObjectSoup(reponse)
    tabLinksOut=[]
    try:
        current=soup.find('section').find("ul",class_='pager').find("li",class_="current")  
    except:
        haveOnePage=HaveOnePage(True)
    else:
        haveOnePage=HaveOnePage(False)

    if(haveOnePage):
        tabLinksOut=getContentOnOnePage(soup)
    else:
        valueCurrent=getIntegersFromString(current.string)
        nbMax=getNumberMaxOfPages(valueCurrent)
        tabLinks=getAllPagesLinks(nbMax,url)
        tabLinksOut=getAllContentsOfPages(tabLinks)
    return tabLinksOut

# Creation des fichiers CSV par Categorie
def CreationCSVdataByCategory(tabUrlCategory,soup):
    namesCat=[]
    namesCat=getAllCategoriesNames(soup)
    number=0
    for url in tabUrlCategory:
        # Extraction de tous les urls de la categorie selectioné
        tabLinksgeted=getContentByCategory(url)  
        
        # Formatage des liens 
        newTabformatLinks=[]
        for tablink in tabLinksgeted:
                newLink=re.sub("../../../","https://books.toscrape.com/catalogue/",tablink)
                newTabformatLinks.append(newLink)
        
    
        # Extraction des contenus de tous les livres d'une Category selectioné
        contentsOfBooks=getContentsOfProducts(newTabformatLinks)
      
        enteteProduit=["universal_ product_code (upc)","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url","urlCategory"]

        # Creation de mon fichier  CSV   
        with open("data"+str(number)+".csv","w",encoding='utf-8')as file:
                writer=csv.writer(file, delimiter=',')
                writer.writerow(enteteProduit)
                for content in contentsOfBooks:
                    writer.writerow(content)
        number=number+1
        
        

       
        
