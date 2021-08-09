from fastapi import FastAPI
from Scrapper import Scraper

app = FastAPI()
quotes = Scraper()

quotes.scrape_data('love') 


@app.get('/{cat}')
async def read_item(cat):
    return quotes.scrape_data(cat) 

