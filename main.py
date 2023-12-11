import random
import webbrowser
import requests
import bs4


valid_letters = "qwertyuiopasdfghjklzxcvbnm"

# hangman
# guess the word game
# limited amount of tries

# game starts: new word puzzle generated w/ details abt how many letters
# ask for letter input
#  if letter inpur exist in word, display letter instead of _____
# else: tries -= 1
# repeat until word is complete or out of tries
# check for invalid entries
# bigger word bank
def hangman():
    wordbank = ["water", "cooler", "summer"]
    word = random.choice(wordbank)
    print("your word has " + str(len(word)) + " letters!")

    # this holds the display of hidden word
    main = ""
    # chances is 7 bc for the while loop its greater than zero and you subtract everytime so you would be at zero
    # when they lose which doesnt work so just saying 1 = lose game over works better
    chances = 10

    # this holds onto all the letters that were guessed
    guesses_made = ""
    while chances > 0:
        # restarts the main so it doesnt get rly long w/ a bunch of ___
        main = ""
        guess = input("What is your guess?")
        guess = guess.lower()
        while guess not in valid_letters or (guess in guesses_made):
            guess = input("Only single letter guesses please, no repeats! What is your guess? ")
            guess = guess.lower()
        # adds to guesses made everytime
        guesses_made += guess
        if guess not in word:
            print("letter not in word!")
            chances -= 1
            if chances == 9:
                print("o")
            elif chances == 8:
                print("\o")
            elif chances == 7:
                print("\o/")
            elif chances == 6:
                print("\o/")
                print(" | ")
            elif chances == 5:
                print("\o/")
                print(" | ")
                print("/")
            elif chances == 4:
                print("\o/")
                print(" | ")
                print(" /\\")
            elif chances == 3:
                print("\o/\\")
                print(" | ")
                print(" /\\")
            elif chances == 2:
                print("/\o/\\")
                print(" | ")
                print(" /\\")
            elif chances == 1:
                print("/\o/\\")
                print(" | ")
                print("_/\\_")
        # runs through every letter in the word, for the first letter, if guessed (in guesses_made),
        # it will print, if not, itll print a _
        for letter in word:
            if letter in guesses_made:
                main = main + letter
            else:
                main += "_"
        if main == word:
            print(word)
            print("You won!")
            break
        print(main)
        if chances == 1:
            print(word)
            print("game over!")
            break

def get_random_words():
    url = 'https://randomwordgenerator.com/'
    response = requests.get(url)
# html = hyper text machine language
    if response.status_code == 200:
        soup = bs4.BeautifulSoup(requests.text, 'html.parser')
        # print(soup)
        word_elements = soup.find_all("li", class_ = "support")
        for words in word_elements:
            print(words)
# hangman()
get_random_words()