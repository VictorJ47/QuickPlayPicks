import requests
from bs4 import BeautifulSoup

genre = "Action"
platform = "PS5"

# Practicing with just one page
#if platform == "PS5" and genre == "Action":
URL = "https://howlongtobeat.com/search_main.php?t=games&page=1&sorthead=popular"  # URL of website to scrape
r = requests.get(URL)  # Send HTTP request and save response from the server in response object, r
soup = BeautifulSoup(r.text, "html.parser")  # BS object created using the raw HTML and parser
titles = soup.findAll("a", attrs={"class": "text_white"})

for title in titles:
    print(title.text)
    
    
    # print(soup.prettify()) #gives the visual representation of the parse tree created from the raw HTML content