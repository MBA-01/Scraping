import requests
from bs4 import BeautifulSoup


# VALID ✅
# One website was scraped successfully (Product links only | for now)

def setup():
    global baseurl,headers,ProductLinks
    baseurl = "https://artisans-dumaroc.com" 
    headers ={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    ProductLinks =[]

def get_prod_link():
    for item in productlist:
        for link in item.find_all('a',href=True):
            ProductLinks.append(baseurl + link['href'])
            break
#_____________________________________

# First Part 
# Scraping all website products

# we'll need to go through all pages by looping
def scrape_all_product():
    global productlist

    setup()
    for x in range(1,16):

        # Everything below is used to scrape one page content 
        r = requests.get(f'https://artisans-dumaroc.com/collections/all-products?page={x}')
        soup = BeautifulSoup(r.content, 'lxml')

        # Specifying the Class name for the products (all products similar class)
        productlist = soup.find_all('div', class_='Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--lap-and-up')

        # for item in productlist:
        #     print(item)
        #     print('____________________________________________')

        # for item in productlist:
        #     for link in item.find_all('a',href=True):
        #         print(link['href'])
        #         # Returning 2 links instead of 1
        #         # Break allows us to get one link only in this situation 
        #         break

        get_prod_link()
    return ProductLinks
lst = scrape_all_product()

print(len(lst))

for i in ProductLinks:
    print(i)
# for each in ProductLinks:
#     print(each)

# print(len(ProductLinks))




#_____________________________________

# Second part 
# Product page scraping

testlink = 'https://artisans-dumaroc.com/collections/all-products/products/ceramic-storage-box'

r = requests.get(testlink, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

print(soup.find('h1',class_='ProductMeta__Title Heading u-h2').text.strip())