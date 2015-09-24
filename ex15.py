# Imports the argv module from sys.
from sys import argv

# Sets the script to read a file name as an argument on launch.
script, filename = argv

# Assign the contence of the file called filename to the var txt.
txt = open(filename)

# Prints string and includes the filename givven as an argument.
print "Here's your file %r: " % filename
print txt.read()

print "Type the file name again:"
file_again = raw_input("> ")

text_again = open(file_again)

print text_again.read()
