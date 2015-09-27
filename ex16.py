from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "Tf you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# Ereasing the contence of the file that was named in the opening the argument.
# Not really required since
# target.truncate()

print "Now I'm going to ask you for three lines."

# Declare a variable to a line of raw_input from the user x3.
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm ging to write these to a file."

# Rewrite the w
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# Write a line in the new file, with the variables declared earlier.
# Drops down to a new line in the new file.
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
# Closes and saves the new file.
target.close()
