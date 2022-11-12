import requests

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
    
# recuperation des contenus ayant une seule page
def getContentOnOnePage(soup):
    titres=soup.findAll("h3")
    urlInfos=[]
    for titre in titres:
        urlInfos.append(titre.find("a")["href"])
    return urlInfos

# Verification de l'existence de plusieurs pages
def HaveOnePage(value):
    return value

#recuperation des contenus dans plusieurs pages
def getAllContentsOfPages(tabLinks):
    allContentsOfPages=[]
    for link in tabLinks:
        reponse=requests.get(link)
        soup=createObjectSoup(reponse.content)
        titres=soup.findAll("h3")
        for titre in titres:
            allContentsOfPages.append(titre.find("a")["href"])
    return allContentsOfPages
  
# focntion principle qui genre le contenu d'une category ayant ou pas plusieurs pages
def getContentByCategory(url):

    reponse=fonctionGetContent(url)
    soup=createObjectSoup(reponse)

    try:
        current=soup.find('section').find("ul",class_='pager').find("li",class_="current")  
    except:
        haveOnePage=HaveOnePage(True)
    else:
        haveOnePage=HaveOnePage(False)

    if(haveOnePage):
        print(getContentOnOnePage(soup))
        # autres instructions
    else:
        valueCurrent=getIntegersFromString(current.string)
        nbMax=getNumberMaxOfPages(valueCurrent)
        tabLinks=getAllPagesLinks(nbMax,url)
        tabLinksOut=getAllContentsOfPages(tabLinks)
    return tabLinksOut
   
# Generation des contenus des livres par categorie
def getContentsOfBooksByCategory(tabLinks):
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
        urlCateg=link

        # ajout des informations dans un tableau
        ContentsOfbooks.append([universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url,urlCateg])
    return ContentsOfbooks

       


