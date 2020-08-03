# 1. TASK: print "Hello World"
print("Hello World")


# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"

# 2a. 
print("Hello", name)	# with a comma

# 2b. 
print("Hello " + name)	# with a +


# 3. print "Hello 42!" with the number in a variable
name = 42
# 3a. 
print("Hello", name, "!")	# with a comma

# 3b. 
# print("Hello " + name)	# with a +	-- this one should give us an error!
#NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
print("Hello %d" % (name))
#best to use print("Hello " + str(name))

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
# 4a. 
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
# 4b.
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

