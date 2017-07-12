def fact(n):
	result=1
	if n > 1:
		for i in range(2,n+1):
			result*=i
		return result

def factorial(n):
	if  0<=n<=1 :
		return 1
	elif (n > 1):
		return n*factorial(n-1)
	else:
		print( "The factorial cannot be calultaed for nagetive number")


for g in range(130):
	print("{0} factorial is {1}".format(g,factorial(g)))

def febonnaci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		nminus1=1
		nminus2=0
		for i in range(1,n+1):
			result =  nminus1+nminus2
			nminus2=nminus1
			nminus1=result
		return result

for g in range(10):
	print(g,febonnaci(g))