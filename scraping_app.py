import requests
from time import sleep
from bs4 import BeautifulSoup
from csv import DictWriter

# values in models dictionary are codes for various car manufacturers on site
models={'alfa romeo':2015,'audi':2019,'bmw':2022,'buick':2025,'cadilac':2026,'chevrolet':2027,
		'crysler':2028,'citroen':2029,'dacia':2031,'daewoo':2032,'daihatsu':2033,'dodge':2035,
		'fiat':2037,'ford':2038,'gaz':2040,'iveco':2049,'jaguar':2051,'jeep':2052,'kia':2053,
		'lada':2055,'lancia':2057,'land rover':2058,'lexus':2059,'mg':2289,'mahindra':2295,
		'mazda':2064,'mercedes':2066,'mini':2067,'mitsubishi':2068,'moskwitch':2070,'great wall':2350,
		'honda':2352,'hummer':2042,'hyundai':2043,'infiniti':2044,'isuzu':2048,'nissan':2071,
		'opel':2073,'peugeot':2074,'pontiac':2075,'porsche':2076,'renault':2079,'rover':2081,
		'saab':2082,'seat':2085,'skoda':2086,'smart':2087,'ssangyong':2089,'subaru':2090,
		'suzuki':2091,'tata':2286,'toyota':2095,'trabant':2096,'uaz':2098,'wolkswagen':2100,
		'volvo':2101,'wartburg':2102,'zastava':2161,'chery':2189,'any':''}

# User input for manufacturer, make year and price to search for
def search_options():
	search_model=input('Which model are you searching for? If irrelevant enter "any".\n ' ).lower()
	while search_model not in models:
		print('\nThere is no that model!')
		search_model=input('Which model are you searching for? If irrelevant enter "any".\n ' ).lower()
	model_num=models[search_model]
	model_url=f'data%5Bgroup_id%5D={model_num}&'
	make_year = input('Which is the minimum make year of vehicle you are searching? If irrelevant enter "any".\n ')
	while make_year.isdigit() == False:
		if make_year == 'any':
			make_year=''
			break
		make_year = input('Which is the minimum make year of vehicle you are searching? If irrelevant enter "any".\n ')
	price=input('Up to which price in EUR to search for?\n ')
	while price.isdigit() == False:
		price=input('Up to which price in EUR to search for?\n ')
	url=f'https://www.kupujemprodajem.com/Automobili/search.php?action=list&data%5Bad_kind%5D=goods&data%5Bcategory_id%5D=2013&{model_url}data%5Border%5D=posted+desc&data%5Bvehicle_make_year_min%5D={make_year}.&data%5Bprice_to%5D={price}&data%5Bcurrency%5D=eur&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bpage%5D='
	return url

# Scraping site https://www.kupujemprodajem.com/ for selected cars
def scraping_cars():
	base_url=search_options()
	page_url = '1'
	all_cars = []
	while page_url:
		res = requests.get(f'{base_url}{page_url}')
		print(f'Now scraping {base_url}{page_url}.......')
		soup = BeautifulSoup(res.text, 'html.parser')
		auto_oglasi = soup.find_all(class_='item clearfix')
		for auto in auto_oglasi:
			all_cars.append({
						'model': auto.find(class_='adName').get_text().replace("\t","").replace("\n",""),
						'cena': auto.find(class_='adPrice').get_text().replace("\t","").replace("\n",""),
						'grad': auto.find(class_='locationSec').get_text().replace("\t","").replace("\n",""),
						'opis': auto.find(class_='adDescription descriptionHeight').get_text().replace("\t","").replace("\n","") 
				})
		try:
			next_btn = soup.find(class_='pagesList clearfix').find(class_='this-page').find_next_sibling('li')
		except:
			next_btn=None
		page_url = next_btn.find('a').get_text() if next_btn else None
		sleep(0.5)
	return all_cars

# write scraped cars to csv file
def write_automobili(all_cars):
	with open("cars.csv",'w', encoding='utf-8') as file:
		headers = ['model','cena','grad','opis']
		csv_writer = DictWriter(file, fieldnames=headers)
		csv_writer.writeheader()
		for auto in all_cars:
			csv_writer.writerow(auto)

# execute scripts
all_cars=scraping_cars()
write_automobili(all_cars)