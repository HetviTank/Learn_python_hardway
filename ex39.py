states = {'Oregon':'OR',
'Florida':'FL',
'California':'CA',
'New York':'NY',
'Michigan':'MI'}

cities = {
'CA':'san francisco',
'MI':'Detroit',
'FL':'Jacksonvile'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('NY state has: ',cities['NY'])
print('Or state has: ', cities['OR'])
print('_'*25)

print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ",states['Florida'])
print('_'*25)

print("Michigan has: ",cities[states['Michigan']])
print("Florida's has: ",cities[states['Florida']])
print('_'*25)

for state,abbrev in states.items():
	print("%s is abbreviated %s" %(state,abbrev))
	print('_'*25)

for abbrev,city in cities.items():
	print("%s has the city %s" %(abbrev,city))
	print('_'*25)

for state,abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev]))

state = states.get('Texas',None)

if not state:print('sorry no texas')

city = cities.get('TX','Does Not Exits')
print("The city for the state 'TX' is %s" %city)

