# import tool to make random choice
import random

# grab word from file when play game


# def grab_word(file):
# with open('test-word.txt', 'r') as file:
#correct_word = file.read().replace('\n', '')
correct_word = (random.choice(open("words.txt", "r").read().split()))
print(correct_word)
# create list for wrong letters
# create list for right letters
# create file


# random choice of word from file

#correct_word = random.choice('test_word.txt')
# ask user to guees the letters
#print("Guess the letters")

def play_again():
    correct_word = (random.choice(open("words.txt", "r").read().split()))
    play_it = input("Do you want to play again? (y/n)")
    if play_it == ("y"):
        guess_letters(correct_word)
    else:
        print("Later hater!")


# create function that shows letters guessed
def guess_letters(word):
    # blank space for guesses
    letters_in_correct_word = ["_" for letter in word]
    right_choices = []
    wrong_choices = []
    tries = 8
    while tries > 0:
        guess = input("guess a letter ")
        if guess in wrong_choices:
            print("You already guessed that!")
        elif guess in right_choices:
            print("Right guess but already guessed it!")
        # check first if the guess is not in the word
        elif guess not in word:
            wrong_choices.append(guess)
            tries -= 1
            print(f'Wrong, you have {tries} more tries')
            print(f'Wrong letters: {wrong_choices}')
            if tries == 0:
                print("You lose. The correct word is", word)
                play_again()
                return
        # guess is in the word
        else:
            right_choices.append(guess)
            for i in range(len(letters_in_correct_word)):
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
            # print(right_choices)
            print(letters_in_correct_word)
            if word == ''.join(letters_in_correct_word):
                print("You won!")
                play_again()
                return

# loop game for when you run out of tries or choose all correct letters


if __name__ == "__main__":
    guess_letters(correct_word)

# def play_game(file):
#     for word in file:


# create a blank board based on the number of letters in the word
# if user guesses before return to random word choice from file
# -1 guesses after guess incorrectly
# end game when user guesses all correct letters
