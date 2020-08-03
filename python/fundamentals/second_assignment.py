x = 70
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")


dog = ('Bruce', 'cocker spaniel', 19, False)
print (dog)
print (dog[0])
# dog[1] = 'dachshund' # ERROR: cannot be modified ('tuple' object does not support item assignment)


# List
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']


# Dictionaries
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        


# find a value or variable's data type
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# find the length
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

# change data type and add
# print("Hello" + 42)			# output: TypeError
print("Hello " + str(42))	# output: Hello 42


total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)


x = 12
if x > 50:
	print("bigger than 50")
else:
	print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
if x > 10:
	print("bigger than 10")
elif x > 50:
	print("bigger than 50")
else:
	print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
	print("smaller than 10")
# nothing happens, because the statement is false   


# For Loops with Range
for y in range (0, 10, 2):
	print(y)
for a in range(5, 1, -3):
	print(a)


# For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz



# For Loops through Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python



# While Loops
for count in range(0,5):
    print("looping - ", count)

print("while looping sample")
# count = 0
while count <= 5:
	print ("looping - ", count)
	count += 1

print("Else statement")
#Else
m = 3
while m > 0:
	print(m)
	m = m - 1
else:
	print("Final else statement")

#Break
print("Break")
for val in "string":
	if val == "i":
		break
	print(val)
# output: s, t, r


print("continue")
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

print("continue II")

y = 3
while y > 0:
    print(y)
    y = y - 1
    print("Final else statement " + str(y))
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1



















