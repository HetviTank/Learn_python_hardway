from sys import argv
script, user_name = argv
prompt = '>'

print ("Hi %s, I'm the %s script." % (user_name, script))
print("I had like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)


print ("where do you live %s?" % user_name)
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))