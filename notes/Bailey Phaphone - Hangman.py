import random
import string
word_bank = ["phoenix", "amazing", "ice cream", "sync", "incantation", "pandemonium", "isosceles", "California",
             "xylophone", "Yggdrasil"]

word = random.choice(word_bank)
guesses = 6
LettersCorrect = []
LettersIncorrect = []
Letters = (len(word))

string1 = word
list1 = list(string1)
print(list1)

alphabet = string.ascii_letters

for i in range(len(list1)):
        if list1[i] == alphabet:
            list1.pop(i)
            list1.insert(i, "*")


print("".join(list1))



