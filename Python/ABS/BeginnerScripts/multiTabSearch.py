#! python3
#multiTabSearch.py - open several search results in separate tabs

import requests, bs4, sys, webbrowser


print("Googling...")
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search links

soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select('.r a')

# TODO: Open a browser tab for each result

numOpen = min(15, len(elems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + elems[i].get('href'))



