name = "Zed A. Shaw"
age = 35 #not a lie
height = 74 #inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall.(Thats %f centimeters.)" % (height, height_cm)
print "He's %d pounds heavy.(Thats %f kilograms.)" % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try and get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
