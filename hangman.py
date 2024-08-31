

"""
There is a gallows to hang a man
the player has to guess a word
each word has a topic
choose select words and topics and choose from them randomly
for each wrong play, a part of the man  is hanged
for each right play, the letter is filled on the gaps
if the man is totally hanged, the game ends

use a dictionary to map word topics to words ------- then choose a random topic and word

they can only guess wrong 7 times
the game starts with a display of the default before fails



define a main function
display the game intro when the game starts
display initial (default) gallows (for fails == 0)
gallows display depends on number of fails -- keep track of fails (variable?) -- increment fail with each wrong guess

display word category (with every guess loop)
display underscores '_' for every character of the chosen word
replace the underscore with the actual character after each right guess
for every failed guess, display current letters (keep track of guessed letters) and next gallows (depending on the fail count)

if the player wins, -------- 'you win!'
if not, 'sorry, the word was ________'
"""








default = r''' 
____________
|          |
|          
|
|
|
|
|
|_________________
'''

first_fail = r'''
____________
|          |
|          o
|
|
|
|
|
|_________________
'''

second_fail = r'''
____________
|          |
|          o
|         / 
|          
|         
|
|
|_________________
'''

third_fail = r'''
____________
|          |
|          o
|         /|
|          
|         
|
|
|_________________
'''

fourth_fail = r'''
____________
|          |
|          o
|         /|\
|          
|         
|
|
|_________________
'''

fifth_fail = r'''
____________
|          |
|          o
|         /|\
|          |
|         
|
|
|_________________
'''

sixth_fail = r'''
____________
|          |
|          o
|         /|\
|          |
|         / 
|
|
|_________________
'''

seventh_fail = r'''
____________
|          |
|          o
|         /|\
|          |
|         / \
|
|
|_________________
'''


game_intro = """
Welcome to Hangman!

Objective: Guess the hidden word before you run out of tries.

Instructions:
1. Guess Letters: You will be prompted to enter a letter. Each correct letter will be revealed in the word.
2. Track Progress: You will see the current state of the word with correctly guessed letters and underscores for the remaining letters.
3. Avoid Mistakes: Each incorrect guess will count against your total number of tries. If you run out of tries, the game is over.
4. Win the Game: You win by correctly guessing all the letters in the word before running out of tries.
5. Lose the Game: The game ends if you use up all your tries without guessing the word.

Good luck and have fun!
"""


word_topics = {
    'animals': ['lion', 'tiger', 'elephant', 'giraffe', 'zebra'],
    'fruits': ['apple', 'banana', 'cherry', 'date', 'grape'],
    'countries': ['canada', 'brazil', 'india', 'japan', 'france'],
    'colors': ['red', 'blue', 'green', 'yellow', 'purple'],
    'sports': ['soccer', 'tennis', 'cricket', 'hockey', 'rugby'],
    'movies': ['inception', 'matrix', 'titanic', 'joker', 'gravity'],
}


import random


def play_game():
    
    topic = random.choice(list(word_topics.keys()))
    word = random.choice(word_topics[topic])
    
    word_letters = list(word)
    all_guesses = ['_' for letter in word_letters]

    fails = 0
    all_gallows = [default, first_fail, second_fail, third_fail, fourth_fail, fifth_fail, sixth_fail, seventh_fail]

    while fails < 7:
        
        current_gallows = all_gallows[fails]

        if all_guesses == word_letters:
            print('\n', ' '.join(all_guesses), '\n\n\n')
            print('Woohoo!👏 You won!', '\n\n\n')
            break

        print(current_gallows, '\n')
        print('Topic:', topic, '\n')
        #print('Word:', word, '\n')
        print(' '.join(all_guesses), '\n')

        guess = input('Guess a letter: ').lower().strip()  # implement error handling for invalid guesses

        if guess in word_letters:
            for i in range(len(word_letters)):
                if guess == word_letters[i]:
                    all_guesses[i] = guess
        
        elif guess not in all_guesses:
            fails += 1

    if fails == 7:
        print(seventh_fail, '\n\n\n', f"sorry, the right word was '{word}'", '\n\n\n')


def main():
    print(game_intro)
    play_game()


if __name__ == "__main__":
    main()