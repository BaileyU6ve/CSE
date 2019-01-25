import random
import string
word_bank = ["Phoenix", "majestic", "ice cream!", "sync", "incantation", "pandemonium", "isosceles", "California",
             "xylophone", "Yggdrasil"]

guesses = 8
word = random.choice(word_bank)
list1 = list(word)
letters_guessed = []
output = []
letters = (len(word))
alphabet = string.ascii_letters
punctuations = string.punctuation

for i in range(letters):
    output.append("*")
print("".join(output))
# print(word)

while guesses > 0 and (len(word)) > 0:
    guess = input("Pick a letter -")
    letters_guessed.append(guess)
    if guess in word:
        print("Correct!")
        # for i in range(len(word)):



