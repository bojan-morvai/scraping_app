from csv import DictReader

# open csv file with scraped cars
def open_file(filename):
	with open(filename,'r',encoding='utf-8') as file:
		csv_reader = DictReader(file)
		return list(csv_reader)

cars_list = open_file('cars.csv')

# user input, sorting options
def sorting_menu():
	query=input('On which parameters would you like to sort cars?\n1) Price\n2) Alphabetical\n3) Make Year \n4) City \n')
	while query not in ('1','2','3','4'):
		print('There is no that choice.')
		query=input('On which parameters would you like to sort cars?\n1) Price\n2) Alphabetical\n3) Make Year \n4) City \n')
	sorting(query)

# sorting by given parameters
def sorting(query):
	if query == '1':
		print('Sorting by price')
		price_sort = sorted(cars_list, key=lambda i: int(i['cena'].replace('.','').replace(',','').replace("\xa0€",'').replace('\xa0din','')))
		for car in price_sort:
			print_car(car)
	elif query == '2':
		print('Sorting alphabetically')
		model_sort = sorted(cars_list, key=lambda i: i['model'])
		for car in model_sort:
			print_car(car)
	elif query == '3':
		print('Sorting by make year')
		year_sort = sorted(cars_list, key=lambda i: i['opis'])
		for car in year_sort:
			print_car(car)
	elif query == '4':
		print('Sorting by city')
		city_sort = sorted(cars_list, key=lambda c:c['grad'])
		for car in city_sort:
			print_car(car)

# print sorting results
def print_car(car):
	desc=car['opis']
	# This is done because there is short description of each car on website, and usually first thing in here is make year
	if desc[0] == '2' and '1':
		make_year = (f'{desc[0]}{desc[1]}{desc[2]}{desc[3]}')
	else:
		make_year='Not Applicable'
	return print(f"The car {car['model']}, make year is {make_year} is at price {car['cena']}, in {car['grad']}")

# execute scripts
sorting_menu()
