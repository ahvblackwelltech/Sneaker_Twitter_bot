import os
from pip._vendor import requests
# website with sneaker pictures
url = "https://www.flightclub.com/air-jordans"

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for sneakers images
if not os.path.exists('sneakers'):
    os.makedirs('sneakers')

# move to new directory
os.chdir('sneakers')


# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('sneaker-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass