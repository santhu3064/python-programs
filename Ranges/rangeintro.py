# a=range(0,100,2)
# print (a)
# print (a[3])
#

# Div7= range(0,10000,13)
# Guess=int(input("Please enter a value to check divisibilty by 13 \n"))
#
# if Guess in Div7:
# 	print ("{} is divisible by 13".format(Guess))
# else:
# 	print("The number is not dvisible by 13")
#

My_range=range(0,100)
New_Range=My_range[3:40:3]
for i in New_Range :
	print (i)

print ("---" *40)

print(range(0,5,2) == range(0,6,2))
print (list(range(0,5,2)))
print(list(range(0,6,2)))


print ("---" *40)
Rev=list(range(1000,900,-13))
for i in Rev:
	print (i)

print(range(0,100)[::-2])

a=range(0,100,2)

b=a[::3]
for i in b:
	print (i)