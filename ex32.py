the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pe', 2, 'dimes', 3 , 'quarters']

for number in the_count:
	print("this is count %d" %number)

for fruit in fruits:
	print("a fruit of types: %s" %fruits)

for i in change:
	print("i got %r" %i)

elements = []

for i in range(0, 6):
	print("adding %d to the list." %i)
	elements.append(i)

for i in elements:
	print("element was: %d" %i)


  