#Python supports the usual logical conditions from mathematics:

    #Equals: a == b
    #Not Equals: a != b
    #Less than: a < b
    #Less than or equal to: a <= b
    #Greater than: a > b
    #Greater than or equal to: a >= b

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Checking if a number is positive:
number = 15
if number > 0:
  print("The number is positive")


#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#One-line if statement:
a = 5
b = 2
if a > b: print("a is greater than b")

#One line, three outcomes:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#and - Returns True if both statements are true
#or - Returns True if one of the statements is true
#not - Reverses the result, returns False if the result is true

#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#You can have if statements inside if statements. This is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Could also be written with and:
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

