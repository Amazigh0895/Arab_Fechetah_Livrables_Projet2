import fonctions
import csv
import re

# le lien de la categorie selectioné
url="http://books.toscrape.com/catalogue/category/books/fiction_10/"

# Extraction de tous les urls de la categorie selectioné
tabLinksgeted=fonctions.getContentByCategory(url)

# Formatage des liens 
newTabformatLinks=[]
for tablink in tabLinksgeted:
            newLink=re.sub("../../../","https://books.toscrape.com/catalogue/",tablink)
            newTabformatLinks.append(newLink)

# Extraction des contenus de tous les livres d'une Category selectioné
contentsOfBooks=fonctions.getContentsOfBooksByCategory(newTabformatLinks)

enteteProduit=["universal_ product_code (upc)","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating","image_url","urlCategory"]

# Creation de mon fichier  CSV   
with open("data.csv","w")as file:
        writer=csv.writer(file, delimiter=',')
        writer.writerow(enteteProduit)
        for content in contentsOfBooks:
            writer.writerow(content)

        
        
    
