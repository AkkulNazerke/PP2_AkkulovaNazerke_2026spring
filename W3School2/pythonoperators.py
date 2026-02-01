print(10 + 5) 
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400) 

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Python has two division operators:

   # / - Division (returns a float)
   # // - Floor division (returns an integer)

x = 12
y = 5

print(x / y)
print(x // y)

#he count variable is assigned in the if statement, and given the value 5: numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Test if a number is greater than 0 and less than 10:
x = 5
print(x > 0 and x < 10)

#Test if a number is less than 5 or greater than 10:
x = 5
print(x < 5 or x > 10)

#Reverse the result with not:
x = 5
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)


#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

#Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)

print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3) 
print(5 + 4 - 7 + 3) 
