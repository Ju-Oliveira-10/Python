#Conditional statements
#Exercise: the condition above is not enought. We you to be a citizen of a memberstate. Add that condition to the IF statement.
age = 18
memberstate = True
if ((age >= 18) & memberstate):
    print("You are eligible to vote in the next 2024 EU elections.")
else:
    print("Sorry, you are not eligible to vote.")

#We can also chain multiple IFs:
grade = 92
if (grade >= 90):
    print("Excellent")
elif (grade >= 80):
    print("Very good")
else:
    print("Good try")

#Looping or cycle statements
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

#Exercise: add 1 more fruit to the list and iterate over the list again
fruits.extend(["orange","grape","kiwi"])
for fruit in fruits:
    print(fruit)

#Exercise: now do the same loop but if the fruit is banana or one of the newly added fruits, don't print them
for fruit in fruits:
    if (fruit == "banana" or fruit == "kiwi"):
        pass
    else:
        print(fruit)
