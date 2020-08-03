#1. Basic - Print all integers from 0 to 150.
for i in range(151):
	print (i)


#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for m in range(5, 1001, 5):
	print(m)


#3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for b in range(101):
	if b % 10 == 0:
		print("Coding Dojo")
	elif b % 5 == 0:
		print("Coding")
	else:
		print(b)


#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for p in range (1, 500000, 2):
	sum += p
print (sum)


#5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for c in range (2018, 0, -4):
	print (c)


#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flex_count(lowNum, highNum, mult):
	for g in range(lowNum, highNum + 1, 1):
		if g % mult == 0:
			print(g)

flex_count(2, 9, 3)


