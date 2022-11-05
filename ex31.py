print("you enter a dark room with two doors.")

door = input("> ")

if door == "1":
	print("there's a giant bear here eating a chees cake.")
	print("1. Take the cake.")
	print("2. cream at the bear.")
	
	bear = input("> ")

	if bear == "1":
		print("the bear eats your face.")
	elif bear == "2":
		print("the bear eats your legs off.")
	else:
		print("well, doing %s is probably better.") %bear

elif door == "2":
	print("you")
	print("1. b")
	print("2. ye")
	print("3. un")

	insanity = input("> ")

	if insanity == "1"  or insanity == "2":
		print("your body survives powered by a mind of jello")
	else:
		print(" the insanity rots your ees into a pool of muck .")

else :
	print("you stumble aroud.")

