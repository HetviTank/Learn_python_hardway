i = 0
numbers = []

while i < 6:
	print("at the top i is %d" %i)
	numbers.append(i)

	i = i+1
	print(" number now: ",numbers)
	print("at the bottom i is %d" %i)

print("the numbers:")

for num in numbers:
	print(num)
 