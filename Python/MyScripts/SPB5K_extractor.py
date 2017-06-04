#! python3
#SPB5K_extractor.py - downloads best ShitpostBot 5000


import requests, bs4, sys, webbrowser, time, os

url = 'http://motherless.com/f/a_franz/images'
os.makedirs('ML Pics', exist_ok=True)


print("Connecting to Facebook Server...")

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


#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.execute_script("window.scrollTo(0, Y)")