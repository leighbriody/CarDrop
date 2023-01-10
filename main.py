import requests
from bs4 import BeautifulSoup

URL = "https://www.donedeal.ie/cars?make=Volkswagen;model:Passat"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

#get the price
p_tags = soup.find_all("p")     
i = 0
for tag in p_tags:
    if(tag['class'][0] =="Card__Title-sc-1v41pi0-4"):
        print("Car Name " , tag.text)
        i = i + 1
    if(tag['class'][0] =="Card__InfoText-sc-1v41pi0-13"):
        print("Car Price " , tag.text)
        i = i + 1

  
   
        
    
