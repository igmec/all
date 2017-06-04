#! python3


import requests, bs4, sys, webbrowser, time, os

url = ''
os.makedirs('ML Pics', exist_ok=True)


print("Connecting to Server...")

try:
    res = requests.get(url)
    res.raise_for_status()
except Exceptin as e:
    print("Error: %s" %(e))
    sys.exit(1)


soup = bs4.BeautifulSoup(res.text, "html.parser")
numPics = soup.select('span[class="active"]')
numPics = numPics[0].getText().split('[ ')
numPics = numPics[1].split(' ]')
numPics = int(numPics[0])
print('Detected '+ str(numPics) + ' images.')

numComplete = 0

#picLinks = soup.select('div[class="content-inner"]')
picLinks = soup.find_all("div", class="thumb-container col-md-3  col-sm-4 col-ms-4 col-mxs-6 col-xs-6 ")


print(len(picLinks))
#print(picLinks[0].prettify())
#print(picLinks[0].get('col-md-12'))




sys.exit(0)


















from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')





brokenURL = []
count = 0






print(len(elems))
browser = webdriver.Firefox(firefox_binary=binary)

for vids in range(len(elems)):
    print(elems[vids].attrs)
    vidID = elems[vids].get('data-video-id')
    vidID = 'https://www.youtube.com/watch?v=' + vidID
    print(vidID)

    browser.get('http://www.clipconverter.cc/')
    mediaElem = browser.find_element_by_id('mediaurl')
    mediaElem.send_keys(vidID)

    dlButton = browser.find_element_by_id('submiturl')
    time.sleep(0.5)
    dlButton.click()
    time.sleep(0.5)


    #Close any other tabs except the first open one (Closes pop-up ad)
    openTabs = browser.window_handles
    for handles in browser.window_handles:
        if len(openTabs) <= 1:
            break
        browser.switch_to_window(openTabs[-1])
        browser.close()
        openTabs = browser.window_handles

    browser.switch_to_window(openTabs[0])
    
    selectElem = browser.find_element_by_partial_link_text('YouTube Video ')    
    #selectElem = browser.find_element_by_css_selector('input')
    #selectElem = browser.find_elements_by_css_selector("input[id='0']")
    #selectElem = browser.find_element_by_id('0')
    print(type(selectElem))
    print(selectElem)
    #print(selectElem.attrs)
    selectElem.click()


    sys.exit(0)


    
    

    
    
    webbrowser.open(vidID)




sys.exit(0)



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
