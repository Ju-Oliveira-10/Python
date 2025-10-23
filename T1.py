
#Exercise 5: Guess the Number (basic game 🎮)
#import random

#number = random.randint(1,20)
#guess = int(input("Guess a number: "))

#if guess < number:
#    print("Too low")
#elif guess > number:
#    print("Too high")
#else:
#    print("You win")

#Exercise 1: Even or Odd List
#numbers = []

#for i in range(5):
#    num = int(input("Enter a number: "))
 #   numbers.append(num)

#for n in numbers:
 #   if n % 2 == 0:
  #      print(f"{n} is even")
   # else:
    #    print(f"{n} is odd")

#Exercise 3: Shopping List
list = []

while True:
    item = input("Add item (or type 'done' to finish):")
    if item.lower() == "done":
        break
    list.append(item)

print("Your shooping list: ", list)

#Exercise 5: Password Strength Checker
password = input("Enter a password: ")

number = any(char.isdigit() for char in password)
character = any(char in "!@#$%&*" for char in password)

if len(password) >= 8 and number and character:
    print("Strong password")
elif len(password) >=6 and number and character:
    print("Medium password")
else: print("Weak password")

#Exercise 2: Temperature Converter
temperature = float(input("Enter the temperature: "))

F = (temperature * 9/5) + 32

print(f"The temperature of {temperature}ºC in fahrenheit is", F)

degrees = input("C/F:" )
temperature = float(input("Enter the temperature: "))

if degrees.upper() == "C":
    F = (temperature * 9/5) + 32
    print(f"The temperature of {temperature}ºC in fahrenheit is", F)
else: print("ERROR")

#Exercise 3: Word Repeater
#Ask the user for a word and a number n, then print the word repeated n times.

word = input("Enter a word: ")
number = int(input("Enter a number : "))

print(word  * number)

#Exercise 4: Find the Maximum
#Ask the user for 5 numbers and print the largest one.
numbers=[]

for i in range(5):
    numb = float(input("Enter a number: "))
    numbers.append(numb)

print("Ther largest number is : ", max(numbers))

#Exercise 5: Palindrome Checker
#Ask the user for a word and check if it’s a palindrome (same forwards and backwards).
word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome")
else: 
    print("The word is not a palindrome")


#Exercise 7: Factorial Calculator
#Ask the user for a number n and compute n! (factorial).

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, 1+number):
    factorial *= i

print(f"The factorial of number {number} is: ", factorial)

#Exercise 8: Multiplication Table
#Ask the user for a number and print its multiplication table up to 10.
number = int(input("Enter a number: "))
n = 0

for i in range(11):
    n = i * number
    print(f"{number} * {i} = ", n)

#Exercise 9: Unique Words
#Ask the user for a sentence and print all unique words.

setence = input("Enter a setence: ").lower()
words = setence.split()
unique_words = set(words)

print(f"The setence has {unique_words} unique words")

#Exercise 10: Guess the Number
#The program randomly picks a number between 1 and 20. The user has to guess until correct.
import random

secret = random.randint(1,20)
number = int(input("Enter a number:"))

if number > secret:
    print("It's too high")
elif number < secret:
    print("It's too low")
else:
    print("Correct the number was ", secret)

#Exercise 11: Reverse a String
#Ask the user for a word and print it backwards.

word = input("Enter a word: ").lower()

print(word[::-1])

#Exercise 12: Even or Odd Numbers
#Ask the user for a number and say whether it’s even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Exercise 13: Count Words in a Sentence
#Ask the user for a sentence and print how many words it has.

setence = input("Enter a setence: ")
words = setence.split()

print("Words in the setence: ", len(words))



#Exercise 14: Simple Calculator
#Ask the user for two numbers and an operator (+, -, *, /), then print the result.~
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
operation = input("Choose a operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error:Division by 0")
else:
    print("Error: Operation invalid")
    

#Exercise 1: Loops + Lists
#Task: Write a program that asks the user for 10 numbers, stores them in a list, then:
#Prints the sum
#Prints the average
#Prints the list sorted

list = []

for i in range(5):
   num = float(input("Enter a number: "))
   list.append(num)

print("Sum:", sum(list))
print("Average", sum(list)/len(list))
print("Sorted list", sorted(list))

#Exercise 3: File Handling
#Task: Ask the user for a sentence and save it to a file called notes.txt. Then read the file back and print its content.

with open("notes.txr", "w") as f:
    sentence = input("Enter a sentence:")
    f.write(sentence)

with open("notes.txr", "r") as f:
    content = f.read()
    print(content)

#Exercise 4: Dictionaries (like a mini-database)
#Task: Create a small contact book. The user can add names with phone numbers. Store them in a dictionary.
# At the end, print all contacts.
contacts = {}

while True:
    name = input("Enter a name (or 'done' to finish):")
    if name.lower() == "done":
        break
    phone = input("Enter a phone number:")
    contacts[name] = phone

for name, phone in contacts.items():
    print(f"{name} : {phone}")

#Exercise 5: Square Numbers with a Loop
#Ask the user for 5 numbers, store them in a list, and print their squares.
numbers = []

for i in range(5):
    numb = int(input("Enter a number:"))
    numbers.append(numb)

squares = [x**2 for x in numbers]

print("Squares:", squares)

#Exercise 7: Simple Login System
#Store usernames and passwords in a dictionary. Ask the user to log in by entering username and password.
usernames ={"Juliana":"Ju","Diogo":"burro"}

username = input("Enter the username:")
password = input("Enter the pass:")

if username in usernames and usernames[username] == password:
    print("Login successful")
else:
    print("Login invalid")

#Exercise 8: Multiplication Table (Function)
#Write a function that prints the multiplication table for a number up to 10.
num = int(input("Enter a number:"))

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

table(num)

#Exercise 9: Save and Load Numbers (File Handling)
#Ask the user for 3 numbers, save them to numbers.txt, then read them back and print them.

with open("numbers.txt", "w") as f:
    for i in range(3):
        number = input("Enter a number:")
        f.write(number + "/n")

with open("numbers.txt", "r") as f:
    numbers = f.readlines()
    print([n.strip() for n in numbers])

# Save numbers
with open("numbers.txt", "w") as f:
    for i in range(3):
        num = input("Enter a number: ")
        f.write(num + "\n")

# Read numbers
with open("numbers.txt", "r") as f:
    nums = f.readlines()
    print("Numbers from file:", [n.strip() for n in nums])