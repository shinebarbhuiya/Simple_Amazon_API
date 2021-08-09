import requests
from bs4 import BeautifulSoup


class Scraper():

    def scraped_data(self, tag):

        # tag = tag.replace("https://www.amazon.in/","https://booster-app.piratebay.workers.dev/")
        # print(tag)
        url = f"https://booster-app.piratebay.workers.dev/dp/{tag}"
        header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.content, 'html.parser')
       
        amaz_list =[]

        try:

            title = soup.find(class_='a-size-large product-title-word-break').text.strip()
            real_price = soup.find('span',class_="priceBlockStrikePriceString a-text-strike").text.strip().replace('₹', '').replace(',', '')
            if soup.find(class_='a-size-medium a-color-price priceBlockBuyingPriceString'):
                price = soup.find(class_='a-size-medium a-color-price priceBlockBuyingPriceString').text.strip().replace('₹', '').replace(',', '')
            else:
                price = soup.find(id='priceblock_dealprice').text.strip().replace('₹', '').replace(',', '')
            
            if soup.find(id='merchant-info'):
                seller = soup.find(id='merchant-info').text.strip()
            else:
                seller = 'Unknown'
            print(seller)

            if soup.find(id='availability'):
                stock = soup.find(id='availability').text.strip()
            else:
                stock = "Out of Stock!"
            print(stock)

        


            item = {
                'Title' : title,
                'Original Price' : real_price,
                'Current Price' : price,
                'Seller' : seller,
                'Stock' : stock
            }

            amaz_list.append(item)
        except:
            amaz_list.append('Sorry, no data found for this item! Maybe try another? ')
            
        
        
        
            

        return amaz_list

        



details = Scraper()

details.scraped_data('B08696XB4B/')