'''
1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
2. Iterate through the following list of animals and print each one in all caps.


  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']


3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.



'''

def count_vowels(word):
    count = 0
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
            count += 1

    return count

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
    print( i.upper() )


for i in range(1,21):
    if i %2 == 0:
        print (i +" is even number.")
    else:
        print (i +" is odd number.")

def sum_of_integers(a, b):
    a = int (input("Enter a number:"))
    b = int (input("Enter a number:"))
    return sum(a, b)