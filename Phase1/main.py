
import fonctions
import csv

url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


reponse=fonctions.fonctionGetContent(url)
soup=fonctions.createObjectSoup(reponse)

produtInfos=[]
enteteProduit=["universal_ product_code (upc)","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url"]

#recuperation des information sur le produit
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
produtInfos.append(universal_product_code)
produtInfos.append(title)
produtInfos.append(price_including_tax)
produtInfos.append(price_excluding_tax)
produtInfos.append(number_available)
produtInfos.append(product_description)
produtInfos.append(category)
produtInfos.append(review_rating)
produtInfos.append(image_url)

print(produtInfos)


# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=',')
   writer.writerow(enteteProduit)
   #ajout de ma liste d'information dans le fichier CSV
   writer.writerow(produtInfos)











