__author__ = 'Osmel Contreras'
__final_Project__ ="Hangman python version"
__name_of_file__ ="playhangman.py"

import random

def start_Up():
    print("\n-----------------Hello, Welcome to Hangman!----------------\n   \n"

          "\n----------------------HOW TO PLAY?-------------------------:\n"
          "* Enter any letter from a-z (lowercase) to guess the unknown word. \n"
          "* You have at maximum of 6 wrong guesses. Guess the word letter by letter. \n"
          "* Blank spaces are represented as ['_'] holding any letter of the Alphabet\n"
          "* REMINDER: You cannot guess the whole word in one input. \n"

          "------------------Stay Alive! Do not die!----------------  \n")
    greet = input("\nPress Enter to Start a New Game :")
    return greet

# Randomly chooses a word from a list
#The words here can be updated anytime by the creator

def word_Bank():
    words = ['logan', 'application', 'pancakes', 'science', 'computer', 'osmel',
         'jenq', 'hangman', 'internet', 'swag', 'keyboard', 'python',
         'university', 'hippo', 'donna', 'sloth', 'mammoth', 'brother',
         'networking', 'hardware', 'software', 'apple', 'windows', 'macintosh',
         'programming', 'motherboard', 'binaries', 'enconding', 'zombies', 'words',
         'chocolate', 'windows', 'flabbergasted', 'gargoyled', 'alligator', 'avengers',
         'phone', 'hard', 'soft', 'narnia', 'kelter', "cats", "ubuntu", "women", "hangman"]

    secret_word = words[random.randrange(0, len(words))]
    return secret_word


#Asks the player to type in a letter
def choose():
    choose_letter = input("\nEnter a letter: \n")
    return choose_letter


#This function replaces the masked letters with the revealed letters
def find_replace(char, secret, mask):
    for index, letter in enumerate(secret):
        if char == letter:
            mask[index] = char
    return mask
#Checks if the chosen letter is inside the secret word.

def check(guess, secret_word, mask):
    if guess in secret_word:
        return find_replace(char=guess, secret=secret_word, mask=mask)

#Graphic of hangman via a list. Each time the user inputs an incorrect answer, more of the hangman is shown.

def figure(wrong):
    total_strikes = []
    picture = [
    '-------------\n',
    '|           |\n',
    '|           O\n',
    '|         +---+\n',
    '|           |\n',
    '|          / |\n',
    '|||       /  |\n',
    '||||||\n']


    if len(wrong) == 1:
        print(picture[0])
        print("\tOpps! ...Almost!")
    if len(wrong) == 2:
        print(picture[0]+picture[1])
        print("\tOpps! ...\n")
    elif len(wrong) == 3:
        print(picture[0] + picture[1] + picture[2])
        print("\tIs this the best you can do?\n")
    elif len(wrong) == 4:
        print(picture[0] + picture[1] + picture[2] + picture[3])
        print("\tWOW...this is just sad!...\n")
    elif len(wrong) == 5:
        print(picture[0] + picture[1] + picture[2] + picture[3] + picture[4])
        print("\tI think you need to concentrate!\n")
    elif len(wrong) == 6:
        print(picture[0] + picture[1] + picture[2] + picture[3] + picture[4] + picture[5] + picture[6])
        print("\tMake your last guess count!\n")
    elif len(wrong) == 7:
        print(picture[0] + picture[1] + picture[2] + picture[3] + picture[4] + picture[5] + picture[6]+picture[7])
        print("\tGAME OVER!!\n")
        replay()


# Asks the the user if they want to play again, if so, the program repeats.
def replay():
    user_Input = input("\nWanna Play Again?\nType 'y' for YES or 'n' for NO: ").lower()
    if user_Input == 'y':
        main()
    elif user_Input == 'n':
        print("\nThank you for playing!")
        exit()
    else:
        user_Input = input("Invalid input, please type 'y' for or any other key to exit ")
        if user_Input == 'y':
            main()
        elif user_Input == 'n':
            print("\nThank you for playing!")
            exit()
    exit()


# Main function that calls for the start_Up,
# initializes the variable strikes
# & prints out the appropriate number of "_" to mask the word.
def main():
    start_Up()
    total_strikes = [  "\n  "]
    strikes = 0
    secret = word_Bank()
    mask = [ "_" for character in secret]
    print(mask)

#Informs the user how many wrong guesses they have.
# If the user guesses correctly, A message appears
# to congratulate them and tells them to keep trying.
# If the user guesses incorrectly, "wrong" appears
# and a strike is added to the count.

    while strikes < 6:
        print("REMINDER: You have %i guess(es) wrong!" % strikes)
        guess = choose()
        if check(guess=guess, secret_word=secret, mask=mask):
            print(mask)
            print ('\n Good Guess! Keep Trying!')

            if mask.__contains__("_"):
                pass
            else:
                print("\n YOU WON!, you guessed the right word! ")
                print("The word was "+ secret)
                replay()
        else:
             strikes += 1

             total_strikes.append(strikes)
             figure(total_strikes)
             print(mask)
             print("\nWrong! Try again!")

main()
replay()
