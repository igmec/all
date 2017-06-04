#! python3
#xkcdDownload.py - downloads all xkcd comics

import requests, bs4, sys, webbrowser, time

print("Downloading XKCD Comics...")
res = requests.get('http://xkcd.com')
res.raise_for_status()

# TODO: Retrieve top search links

for x in range(100):
    print("Counted " + x + " out of 100", end='\r')
    time.sleep(500)

sys.exit(0)



soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select('.r a')

# TODO: Open a browser tab for each result

numOpen = min(15, len(elems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + elems[i].get('href'))



