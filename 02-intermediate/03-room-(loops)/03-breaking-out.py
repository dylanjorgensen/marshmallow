while guesses_left > 0:
    guess = int(raw_input("What is your guess"))
    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
else:
    print "You lose"
