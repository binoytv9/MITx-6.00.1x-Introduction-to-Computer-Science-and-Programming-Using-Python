print "Please think of a number between 0 and 100!"

start = 0
stop = 100

while True:
	guess = (start+stop)//2
	print "Is your secret number %s?" %guess

	indicater = raw_input("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.")

	if len(indicater) != 1 or indicater not in 'chl':
		print "Sorry, I did not understand your input."
		continue
	else:
		if indicater == 'l':
			start = guess
		elif indicater == 'h':
			stop = guess
		else:
			print "Game over. Your secret number was: %s" %guess
			break
