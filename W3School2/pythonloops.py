#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

