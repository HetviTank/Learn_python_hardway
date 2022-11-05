def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("you have %d chess!" % cheese_count)
	print("you have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get  blanket. \n")

print("we can just")
cheese_and_crackers(10,20)

print("or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+3)

print("and we can combine the two")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+300)