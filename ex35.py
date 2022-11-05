from sys import exit

def gold_room():
	print("this room is full of gold")

	next = input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)

	else:
		dead("you greedy bstard!")


def bear_room():
	print("there is a bear here.")
	print("the bear has a bunch  of honey.")
	bear_moved = False

	while True:
		next = input("> ")

		if next == "take honey":
			dead("the bear looks at you")
		elif next == "taunt bear" and not bear_moved:
			print("the bear get pissed off the door.")
			bear_moved = True
		elif next == "taunt be" and bear_moved:
			dead("the bear gets pissed off and chews.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("i got no idea")

def cthulhu_room():
	print("here you see the great evil.")
	print("he, it, whatever stares at you and you go .")

	next = input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that we  tsty!")
	else:
		cthulhu_room()

def dead(why):
	print (why, "good job!")
	exit(0)

def start():
	print("you are in a dark room")
	print("there is door to your")

	next = input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room")

start()
