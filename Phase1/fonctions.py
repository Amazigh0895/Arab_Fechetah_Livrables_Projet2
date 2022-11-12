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


