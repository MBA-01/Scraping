import requests
from bs4 import BeautifulSoup
from Scarping_1 import ProductLinks
# VALID #✅
# One website was scraped successfully (Product links only | for now)
print(ProductLinks)




print(x)

def setup():
    global baseurl, headers,testlink,product_dic_lst
    baseurl = "https://artisans-dumaroc.com" 

    headers ={
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    product_dic_lst = []
# Second part 
# Product page scraping (product details information)

    #testlink = 'https://artisans-dumaroc.com/collections/all-products/products/ceramic-storage-box'


def scrape_product_info():
    setup()
    for itemLink in ProductLinks :
    
        r = requests.get(itemLink, headers=headers)
        soup = BeautifulSoup(r.content, "lxml")

        name = soup.find('h1',class_='ProductMeta__Title Heading u-h2').text.strip()
        price = soup.find('span',class_='ProductMeta__Price Price Text--subdued u-h4').text.strip()
        desc = soup.find('div', class_='Rte').text.strip()

    ## ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
    
    ##Images = soup.find_all("img",class_='Image--fadeIn lazyautosizes Image--lazyLoaded')
    # need to review the Image part (takes more time)
    # https://stackoverflow.com/questions/73797759/scrape-images-url-using-beautifulsoup
    # https://www.geeksforgeeks.org/image-scraping-with-python/

        product = {
            'name':name,
            'price':price,
            'description':desc.split("\n")
        }

        product_dic_lst.append(product)

    return product_dic_lst

print(scrape_product_info())
result = scrape_product_info()

print(result)


# print(product)
# print(name)
# print(price)

# for i in desc.split("\n"):
#     print(i)

#print(Images)