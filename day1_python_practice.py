colour = input("Enter a colour: ")
pluralNoun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + colour)
print(pluralNoun + " are blue")
print("I love " + celebrity)

#Build a Calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2) #This will not consider decimal number
Add = float(num1) + float(num2)
Subtract = float(num1) - float(num2)
Multiply = float(num1) * float(num2)
Divide = float(num1) / float(num2)
command = input("Enter command:\n Choose between: (Add, Subtract, Multiply, Divide): ")
if command == "Add": print(Add)
elif command == "Subtract": print(Subtract)
elif command == "Multiply": print(Multiply)
elif command == "Divide": print(Divide)
else: print("Invalid command")

#Ask the user to enter a sentence. If it’s more than 20 characters, say “Too long!”, else print “Nice and short!”
sentence = input ("Enter a sentence: ")
length = len(sentence)
if length > 20:
    print ("Too long!")
else:
    print ("Nice and short!")

name = input("What is your name?: ")
color = input("What is your favorite color?: ")
print("Hello " + name, "! Wow, " + color, "is a great color!")

age = input("How old are you (Answer in years)?: ")
months = str (float (age) * 12)
print("Your age in months is = " + months)

# Full Sentence Generator
name = input("What is your name?: ")
verbs = input("What is your favorite hobby?: ")
noun = input("What is your favourite fruit?: ")
print(name + " loves to " + verbs + " with an " + noun + ".")

# Reverse word
sentence = input("Print a sentence to reverse: ")
print("Reverse sentence is ", sentence[::-1])

#Two Numbers, One Sentence
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum of", num1, "and", num2, "is", num1 + num2,".")
print(f"The sum of {num1} and {num2} is {num1 + num2}.")