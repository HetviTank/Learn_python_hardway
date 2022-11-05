from sys import argv
from os.path import exists

script,from_file, to_file = argv

print("copying from %s to %(from_file, to_file))
in_file = open(from_file)
indata = in_file.read()

print("the input file is %d bytes long" %len(indata))
print("does the output file exist? %r" %exists(to_file)
print("Ready, hit RETURN to continue, CTRL-C to abort."
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("alright, all done.")

out_file.close()
in_file.close()

