name=str(input("please enter your name \n"))
age=int(input("Please enter you age \n"))

if ( age > 18 ) and ( age < 30 ):
	print ("Congrats {0} you are eligible for to go on a 18 30 holiday".format(name))
elif age < 18 :
	print ("sorry {1} you are {0} years less age than elgible".format((18-age),name))
else:
	print("We are sorry {0} you had exceeded the age limit eligible for trip".format(name))

