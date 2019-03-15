from bs4 import BeautifulSoup
import requests 

my_html = 'https://www.newsweek.pl/'
source = requests.get(my_html).text
soup = BeautifulSoup(source, 'html.parser')

print(soup.get_text())