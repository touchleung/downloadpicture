#python3
#downloadXkcd.py - Downloads every single XKCD comic.

import requests
import os, bs4

url = 'http://xkcd.com'
os.chdir('C:\\MyPythonScript')
os.makedirs('xkcd', exist_ok=True)             #store comics in ./xkcd
i=0
#while not url.endswith('#'):
while i < 3:
    #Download the page.
    print('Downloadint page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    #Find the URL of comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        #Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        #Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    i = i + 1
print('Done.')