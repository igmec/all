import requests
import bs4


res = requests.get('http://nostarch.com')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
    
nsSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(nsSoup))
