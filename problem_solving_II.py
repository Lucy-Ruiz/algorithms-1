from cgitb import text
import random
# Task 1 reversed string
#. create an empty string to save the reversed word
#. ask the user for a word
#. obtain the length of the word
#. create a for loop to go through out each index 
#. use range function to get a series of numbers
#. -1 to len to start in the last letter of the word
#. -1 to stop in 0 which would be the first index
#. -1 as a step to go 1 by one in reverse
#. concat input including index into the empty string
#. print variable containing the new string reversed

def reverse_string(word):
    item_reversed = ''
    for i in range(len(word) - 1, - 1, - 1):
        item_reversed += (word[i])
    print(item_reversed)
    return item_reversed

reverse_string()

# Task 2 capitalized letter
#. create an empty string to save capitalized string
#. ask user for a string of two or more words
#. create a for loop to go through each index and capitalize first letter of each word
#. apply range to the len of the word to go 1 by 1 'til the end
#. employ conditionals to determine which letter needs to be capitalized
#. if index is equal to 0 or an space it needs to be capitalized
#. acces to the space between letter substracting 1 to the index
#. use else to print the letter that don't require modifications
#. print outside the loop the capilized words

def capitalize_letter():
    cap_words = ''
    words_to_cap = input('Enter two or more words: ')
    for i in range(0, len(words_to_cap), 1):
        if i == 0:
            a = words_to_cap[i].capitalize()
            cap_words += a
        elif words_to_cap[i - 1] == ' ':
            b = words_to_cap[i].capitalize()
            cap_words += b
        else:
            c = words_to_cap[i]
            cap_words += c
    print(cap_words)

capitalize_letter()

#Task 3 palindrome
#. define function 
#. create an empty string
#. create a for loop to remove spaces from argument to facilitate reading
#. inside the loop save new string without spaces
#. save in a new variable the function reverse_string 
#. use conditional to compare the text without spaces to the reversed text

def palindrome(text_to_palindrome):
    text_to_palindrome_updated = ''
    for i in range(0, len(text_to_palindrome), 1):
        if text_to_palindrome[i] != ' ':
            without_space = text_to_palindrome[i]
            text_to_palindrome_updated += without_space
    reversion = reverse_string(text_to_palindrome_updated)
    print(f'This is the original text: {text_to_palindrome}')
    if text_to_palindrome_updated == reversion:
        print(f'This is a palindrome: {text_to_palindrome_updated}')
    else:
        print('Try again')

is_this_palindrome = 'never odd or even'
palindrome(is_this_palindrome)