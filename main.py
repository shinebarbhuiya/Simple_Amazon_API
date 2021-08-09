from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
details = Scraper()

# details.scraped_data('https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/')

@app.get('/{ASIN}')
async def show_item(ASIN):
    return details.scraped_data(ASIN)