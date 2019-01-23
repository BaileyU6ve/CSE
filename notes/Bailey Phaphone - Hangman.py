import random
import string
word_bank = ["Phoenix", "majestic", "ice cream!", "sync", "incantation", "pandemonium", "isosceles", "California",
             "xylophone", "Yggdrasil"]

guesses = 8
word = random.choice(word_bank)
list1 = list(word)
letters_guessed = []
letters = (len(word))
alphabet = string.ascii_letters
guess = input("Guess a letter-")

letters_guessed.append(guess)

for i in range(list1):
  