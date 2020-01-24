from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/pl-en/p/pl?d=grafik+cards'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
# graps each producks
containers = page_soup.find_all("div", {"class": "item-container"})

print(len(containers))


for container in containers:
    brand = container.find("div", {"class": "item-info"}).a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    prince_container = container.find_all("li", {"class": "price-current"})
    price = prince_container[0].text.strip()

    print("brand:" + brand)
    print("product_name: " + product_name)
    print("price" + price)






