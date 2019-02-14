n = int(input("Please think of a number between 0 and 100!"))
hi = 100
lo = 0
guessed  = False

while not guessed:
    guess = (hi+lo)//2
    print("Is your secret number " + str(guess) + " ?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if inp == 'c':
        guessed = True
        print("Game Over. Your secret number was: "+str(guess))
    elif inp == 'l':
        lo = guess
    elif inp == 'h':
        hi = guess
    else :
        print("Sorry, I did not understand your input.")
