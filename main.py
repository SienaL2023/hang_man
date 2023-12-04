import random

# hangman
# guess the word game
# limited amount of tries

# game starts: new word puzzle generated w/ details abt how many letters
# ask for letter input
#  if letter inpur exist in word, display letter instead of _____
# else: tries -= 1
# repeat until word is complete or out of tries
def hangman():
    wordbank = ["water", "cooler", "summer"]
    word = random.choice(wordbank)
    print("your word has " + str(len(word)) + " letters!")

    # this holds the display of hidden word
    main = ""
    # chances is 7 bc for the while loop its greater than zero and you subtract everytime so you would be at zero
    # when they lose which doesnt work so just saying 1 = lose game over works better
    chances = 7

    # this holds onto all the letters that were guessed
    guesses_made = ""
    while chances > 0:
        # restarts the main so it doesnt get rly long w/ a bunch of ___
        main = ""
        guess = input("What is your guess?")
        # adds to guesses made everytime
        guesses_made += guess
        if guess not in word:
            print("letter not in word!")
            chances -= 1
            if chances == 6:
                print("o")
            elif chances == 5:
                print("\o")
            elif chances == 4:
                print("\o/")
            elif chances == 3:
                print("\o/")
                print(" | ")
            elif chances == 2:
                print("\o/")
                print(" | ")
                print("/")
            elif chances == 1:
                print("\o/")
                print(" | ")
                print(" /\\")
        # runs through every letter in the word, for the first letter, if guessed (in guesses_made),
        # it will print, if not, itll print a _
        for letter in word:
            if letter in guesses_made:
                main = main + letter
            else:
                main += "_"
        if main == word:
            print("You won!")
            break
        print(main)
        if chances == 1:
            print("game over!")
            break
hangman()