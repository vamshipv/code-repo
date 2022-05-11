import requests
import bs4

URL = 'https://terion.in/#/'
page = requests.get(URL)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
res = soup.find(id = 'v-btn__content')
print(res)
