# Python Web Scraping App
File 'scraping_app.py' scrape serbian website https://www.kupujemprodajem.com for used cars based on few user input parameters:
  - car manufacturer
  - make year
  - price
Scraping is done using BeautifulSoup, and after scraping, application write results(car model, price, short description, city) to new csv file called "cars.csv"

File 'cars_statistics.py' read CSV file 'cars.csv' and sort all results by some user input:
  - price
  - alphabetically
  - make year
  - city
