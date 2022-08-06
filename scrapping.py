import requests
from bs4 import BeautifulSoup

url = 'https://www.udocz.com/apuntes/62675/fisica-universitaria-sears-zemansky-13va-edicion-solucionario'

response = requests.post(url)
page = BeautifulSoup(response.text, "html.parser")

VIEWSTATE = page.select_one("#__VIEWSTATE").attrs["value"]
VIEWSTATEGENERATOR = page.select_one("#__VIEWSTATEGENERATOR").attrs["value"]
EVENTVALIDATION = page.select_one("#__EVENTVALIDATION").attrs["value"]
btnDocument = page.select_one("[name=btnDocument]").attrs["value"]

data = {
  '__VIEWSTATE': VIEWSTATE,
  '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
  '__EVENTVALIDATION': EVENTVALIDATION,
  'btnDocument': btnDocument
}
response = requests.post(url, data=data)
with open('/Downloads', 'wb') as f:
    f.write(response.content)