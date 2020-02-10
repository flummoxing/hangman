# Author: Alexa Langen
# Date: 2/1/20
# Description: A game of hangman


def print_word(word_list):
    """Takes a list of letters and returns them as a string with added spaces for legibility"""
    str1 = ""

    for ele in word_list:
        str1 += (ele + " ")

    print(str1, "\n")


def letter_in_word(word, letter):
    """Checks if the letter is in the word."""
    for s in word:
        if s.upper() == letter.upper():
            return True

    return False


def already_guessed(guessed_so_far, new_letter):
    """
    Takes two string parameters: a list of letters already guessed, and a new letter.
    Returns True if letter has already been guessed, otherwise returns False.
    """
    for s in guessed_so_far:
        if s == new_letter:
            return True
    return False


def hide_word(secret_word):
    """Replaces secret word with underscores."""
    hidden_word = list(secret_word)
    length = len(hidden_word)

    for i in range(0, length):
        hidden_word[i] = '_'

    return hidden_word


def update_word(secret_word, word_so_far, new_letter):
    """Gradually fills in secret word with letters as they are guessed correctly."""

    length = len(secret_word)

    for i in range(0, length):
        if secret_word[i] == new_letter:
            word_so_far[i] = new_letter

    return word_so_far


play = True

while play:
    secret_word = "HANGMAN" # Later let this be changed. Has spaces now for comparison
    word_so_far = hide_word(secret_word)
    secret_word_list = [c for c in secret_word] #To compare with word_so_far, which is a list.
    guessed_so_far = "" # Keeps track of letters player has already guessed
    strikes = 0

    print("Welcome to Hangman! Try to guess the following word. You get 6 strikes! \n")
    print_word(word_so_far)

    while word_so_far != secret_word_list and strikes != 6:
        new_letter = input("Guess a letter: \n")

        if already_guessed(guessed_so_far, new_letter):
            print("You've already guessed that letter! Try again.")

        elif letter_in_word(secret_word, new_letter):
            word_so_far = update_word(secret_word, word_so_far, new_letter)
            guessed_so_far += new_letter

        elif not letter_in_word(secret_word, new_letter):
            strikes += 1
            guessed_so_far += new_letter
            print("Nope! You get a strike! You have", strikes, "so far. \n")
            print("Here are the letters you've guessed so far: ", guessed_so_far, "\n")

        print_word(word_so_far)

    if word_so_far == secret_word_list:
        print("You did it! The secret word was: ", secret_word)

    elif strikes == 6:
        print("GAME OVER!")

    again = str(input("Would you like to play again with the same word? Type Y or N."))
    if again.upper() == "N":
        play = False

