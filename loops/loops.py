# name=input("please enter your name \n")
# age=int(input("how old are you {0} \n" .format(name)))
# print (age)
# if age >= 18:
# 	print ("you sre old enough to vote")
# # else:
# 	print ("you are still young")
print ("Please guessa number")
guess=int(input())
if guess > 5:
	print ("please enter a number lower than 5")
	guess=int(input())
	if guess==5:
		print ("you had guessed correctly")
	else:
		print("you had exceeded your attempts and guess is wrong")
elif guess < 5:
	#print ("Guess a number greater than {0}".format(guess))
	guess=int(input())

	if guess==5:
		print ("you had guessed correctly")
	else:
		print("you had exceeded your attempts and guess is wrong")
else:
	print("You guessed it correctly on first attemp")