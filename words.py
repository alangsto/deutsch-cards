import random
from german_nouns.lookup import Nouns

nouns = Nouns()


def select_word():
    word, _ = random.choice(list(nouns.index.items()))
    return nouns[word][0]

def check_user_input(word, gender):
    if word['genus'] == gender:
        return True
    else:
        return False

while True:
    word = select_word()
    print("Word: ", word['flexion']['nominativ singular'])
    gender = input("Enter the gender of the word: ")
    if check_user_input(word, gender):
        print("Correct!")
    else:
        print("Wrong. Try again.")

