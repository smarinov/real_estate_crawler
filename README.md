# Real Estate Crawler with Scrapy
Real estate crawler for https://www.alo.bg 

## How it works?
### The RealEstateSpider crawls through your desired URL and gathers the following data for each listing:
- ID
- Title
- Construction type
- Construction year
- Square meters
- Floor
- Price
- Location
- URL

### Features
- The pipeline takes care for creating a local database (SQLite), automatically connects to it and stores scraped data
- The download delay setting is set to 0.1 seconds so the crawler avoids HTTP 429 Error (Too Many Requests)
- Crawl through all possible pages and auto stop once it reaches the last page
- Uses the "unicodedata" library to avoid storing corrupted characters in the database
- Option to export data to a .tsv file

## How to set it up?
- Clone the repository
- Navigate into it and follow one of the steps below
### Manually run the project
1. Create a virtual environment and activate it:
- "python -m venv venv"
- "source venv/bin/activate"
2. After activating the virtual environment install all the required packages mentioned in the requirements.txt:\
"pip install -r requirements.txt"
3. Run main.py (python3 main.py)
### Automatically run the project
1. Run "start.bat" file

## How to use?
1. Input your URL
2. Wait for the crawler to finish and access the gathered data