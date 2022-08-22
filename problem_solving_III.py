#Task 1 happy number
#. define function with one argument to get number
#. transform number into string to separate digits
#. create a for loop to obtain each digit and save it in a variable
#. transform each string value into a integer to obtain squares
#. sum both values
#. define second function to obtain happy number
#. new variable to save number
#. create an empty list to add result of squares if they aren't and compare if they were
#. create a while loop since I don't know how many times it will be iterated
#. update parameter when calling function squares to save each new number
#. if the new value is different from 1, append it to the list if it's not in
#. break cycle of new value different from one if it's already in the list
#. if value is equal to 1 print that is a happy number
#. if value is different from 1 print that is an unhappy number
#. print the list of value to check the number that were included 

def squares(initial_number):
    transformed_num = str(initial_number)
    result = 0
    for character in transformed_num:
        digits = int(character)
        digits **= 2
        result += digits
    return result

def happy_number(number):
    new_value = number
    list_of_values = []
    while new_value != 1:
        new_value = squares(new_value)
        if new_value not in list_of_values:
            list_of_values.append(new_value)
        else:
            break    
    if new_value == 1:
        print('It\'s a happy number')
    else:
        print('It\'s an unhappy number')
    print(list_of_values)
happy_number(4)

#Task 2 prime numbers
#. define the function 
#. use range to stablish number from 1 to 100
#. create a for loop to go through each of the numbers
#. set a conditional to divide the number by one and modulus by itself

def print_primes():
    for i in range(1, 101, 1):
        prime = True
        for x in range(2, i, 1):
            if i % x == 0:
                prime = False
        if prime == True:
            print(i)

print_primes()

#Task 3 Fibonacci

#. define the function
#. create a for loop with a range to run from 1 upto 100
#. initiate out of the loop two variables in 1
#. print previous to create Fibonacci sequence
#. create a new number variable to sum the last and previous numbers
#. substitute values of variables to update them with the last two digits each


def fibonacci():
    actual_number = 1
    previous_number = 1
    for i in range(1, 101, 1):
        print(previous_number)
        new_number = previous_number + actual_number
        previous_number = actual_number
        actual_number = new_number

fibonacci()
