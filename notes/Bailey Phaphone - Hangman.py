import random
import string
word_bank = ["phoenix", "majestic", "ice cream!", "sync", "incantation", "pandemonium", "isosceles", "California",
             "xylophone", "Yggdrasil"]

word = random.choice(word_bank)
guesses = 6
LettersCorrect = []
LettersIncorrect = []
Letters = (len(word))

string1 = word
list1 = list(string1)
print(list1)
punctuations = string.punctuation
alphabet = string.ascii_letters


for i in range(len(list1)):
        if list1[i] < "z":
            list1.pop(i)
            list1.insert(i, "*")

print("".join(list1))