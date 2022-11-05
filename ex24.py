print("Let's practice everything.")
print("you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = ("""
\tThe lovely world
with logic so firmly plnted
cannot discern \n the needs of love
nor comprehend passion from intuition
\n\t\twhere there is none.
""")

print("--------")
print(poem)
print("----")

five = 10-2+30-6
print("this should be five:%s" %five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans /1000
	crates = jars/100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print (" with :%d" % start_point)
print("done: %d %d" %(beans, jars))

start_point = start_point / 10 
print( "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))