import random

# hangman
# guess the word game
# limited amount of tries

# game starts: new word puzzle generated w/ details abt how many letters
# ask for letter input
#  if letter inpur exist in word, display letter instead of _____
# else: tries -= 1
# repeat until word is complete or out of tries

wordbank = ["water", "cooler", "summer"]

word = random.choice(wordbank)
print("your word has " + str(len(word)) + " letters!")