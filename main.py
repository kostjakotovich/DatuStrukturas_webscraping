import requests
from bs4 import BeautifulSoup

adress = "https://www.prakse.lv/vacancy/list"

html_text = requests.get(adress)

print(html_text)