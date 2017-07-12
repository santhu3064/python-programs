CorrectGuess=[5]
QuitGuess=0
guess=int(input("Please guess a number \n"))
while guess  not in CorrectGuess:
	if (guess == 0):
		print("you have slected option t quit)")
		break
	elif (guess < 5):
		guess=int(input("Please guess a number greater than {0} \n".format(guess)))
	else:
		guess=int(input("Please guess a number less than {0} \n".format(guess)))
print("selected option is correct")

