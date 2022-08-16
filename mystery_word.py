# import tool to make random choice
import random

# grab word from file when play game


# if user guesses before return to random word choice from file
def play_again():

    play_it = input("Do you want to play again? (y/n)")
    if play_it == ("y"):
        guess_letters()
    else:
        print("Later hater!")


# create function that shows letters guessed
def guess_letters():
    word = (random.choice(open("words.txt", "r").read().split()))
    print(word)
    # blank space for guesses
    letters_in_correct_word = ["_" for letter in word]
    print(f'Number of letters to guesss: {len(word)}')
    right_choices = []
    wrong_choices = []
    tries = 8
    while tries > 0:
        guess = input("guess a letter ")
        if len(guess) > 1:
            print("Invalid input guess again")
        elif guess in wrong_choices:
            print("You already guessed that!")
        elif guess in right_choices:
            print("Right guess but already guessed it!")
        # check first if the guess is not in the word
        elif guess not in word:
            wrong_choices.append(guess)
# -1 guesses after guess incorrectly
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
    guess_letters()
