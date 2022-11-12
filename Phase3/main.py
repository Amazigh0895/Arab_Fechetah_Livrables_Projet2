import fonctions
import csv
import re
url="http://books.toscrape.com/"
urlCata="http://books.toscrape.com/catalogue/"

reponse=fonctions.fonctionGetContent(url)
soup=fonctions.createObjectSoup(reponse)

urlsCartegories=[]
urlsAllPages=[]
contentOfallurlsPages=[]

# Recuperation de toutes les urls des catégories grace a la fonction getAllCategoriesLinks(soup)
urlsCartegories=fonctions.getAllCategoriesLinks(soup,url)

fonctions.CreationCSVdataByCategory(urlsCartegories,soup)


"""
# Recuperation de toutes les urls des pages grace a la fonction fonctionGetUrlsOfAllPages(soup,urlCata)
urlsAllPages=fonctions.fonctionGetUrlsOfAllPages(soup,urlCata)
# Recuperation de tous le contenu tout confondu grace a la fonction getAllContentsOfPages(urlsAllPages)
contentOfallurlsPages=fonctions.getAllContentsOfPages(urlsAllPages)

# Formatage des liens 
newTabformatLinks=[]
for link in contentOfallurlsPages:
    newTabformatLinks.append(urlCata+link)
                  

# Recuperation de tous le contenu des produits sur tout le site grace a la fonction getContentsOfProducts(contentOfallurlsPages)
contentOfAllProducts=fonctions.getContentsOfProducts(newTabformatLinks)

enteteProduit=["universal_ product_code (upc)","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]
# Creation de mon fichier  CSV contenant toutes les donnees du site tout confondu   
with open("data.csv","w")as file:
        writer=csv.writer(file, delimiter=',')
        writer.writerow(enteteProduit)
        for content in contentOfAllProducts:
            writer.writerow(content)
"""