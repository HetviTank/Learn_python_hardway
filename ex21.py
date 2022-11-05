def add(a,b):
	print ("ADDING %d +%d" % (a, b))
	return a + b

def subtract(a, b):
	print("MULTIPLYING %d - %d " %(a,b))
	return a-b
def multiply(a, b):
	print ("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print ("DIVIDING %d / %d" % (a, b))
	return a / b

age = add(30,40)
height = subtract(98,4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d" % (age, height))



print("here is a puzzle")

what = add(age,subtract(height, multiply(weight, divide(iq,2))))
	
print("that becomes:" , what, "can you do it by hand?")