#! python3
#xkcdDownload.py - downloads all xkcd comics

import requests, bs4, sys, webbrowser, time, os



soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('#comic img')




















'''
url = 'http://xkcd.com'
os.makedirs('xkcd Comics', exist_ok=True)

print("Connecting to xkcd Comics...")

brokenURL = []
count = 0

while not url.endswith('#'):

    #Download comic's page
    print("Downloading Page %s..." %url)
    res = requests.get(url)

    try:
        res.raise_for_status()

    except Exception as e:
        print("Error loading page... %s" %(e))
        for a in range(5,0,-1):
            print("Retrying in:" + str(a), end='\r')
        continue
        

    #Find comic url
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('#comic img')
    try:
        imgurl = 'http:' + elems[0].get('src')
        
        #Request image from server and open new file

        res2 = requests.get(imgurl)
        try:
            res2.raise_for_status()

        except Exception as e:
            print("Error loading image... %s" %(e))
            for a in range(5,0,-1):
                print("Retrying in:" + str(a), end='\r')
            continue
        
        imgFile = open('xkcd Comics/' + elems[0].get('alt') + '.png', 'wb')

        #Save image and close file
        for chunk in res2.iter_content(100000):
            imgFile.write(chunk)

        imgFile.close()
        count+=1
        print('Comic downloaded')
        
    except (IndexError, Exception) as e:
        brokenURL.append(url)
        print("Image not found on page. Error: %s" %(e))

    #Find link to previous comic, reset url to that comic
    prevElem = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevElem.get('href')

    

print("\n\n===================================\nDownload Complete\n===================================\n")

print('==========BROKEN URLs==============')

for u in brokenURL:
    print(u)
    
print("===================================")
'''
