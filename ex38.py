ten_things = "apples oranges crows telephone"

print("wait theere's not 10 things in that ")

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn"]

while len(stuff) != 5:
	next_one = more_stuff.pop()
	print("adding:", next_one)
	stuff.append(next_one)
	print("there's %d items now." %len(stuff))

print("there we go:",stuff)

print("let's do some things with stuff.")


print( stuff[1])
print (stuff[-1])
print (stuff.pop())
print (stuff)
print ('#'. join(stuff[3:5]))