import math
# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nuthin'."

def area_tri(radus):
    """Function for working out the area of a circle"""
    area = (radus**2) * math.pi
    print "The area of the circle is %fcm squared" % area

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
area_tri(5)
