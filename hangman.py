import random
from words import palabras
import string

def valid(palabras):
    word = random.choice(palabras) #escoge algo al azar de la lista
    while '-' in word or ' ' in word:
        word = random.choice(palabras)
    return word.upper()

def hangman():
    word = valid(palabras)
    word_letters = set(word) #letras en la palabra
    alpabeth = set(string.ascii_uppercase)
    used_letters = set() #letras adivinadas
    
    lives = 7

    #obtener input de usuario
    while len(word_letters) >0 and lives > 0:
        #letras usadas
        #''.join(['a','b','cd']) --> 'a b cd' 
        print('You have', lives, 'lives left and You have used these letters: ',''.join(used_letters))

        #cual es la palabra actual (P L BR )
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alpabeth - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else: 
                lives = lives - 1 
                print('Your letter is not in the word.')

        elif user_letter in used_letters:
            print('You already used that character. Try again')
        else:
            print('Invalid character. Try again.')
    #llega aqui cuando len(word_letters) == 0 o cuando lives == 0
    if lives == 0:
        print('You died. The word was',word)
    else:    
        print('You guessed the word correctly', word, '!!')


hangman()
#user_input = input('Type something: ')

