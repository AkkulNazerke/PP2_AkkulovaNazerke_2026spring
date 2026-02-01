#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple) 

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) 

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#-1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists 

#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 

#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) 

#Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

#Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

#Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) 

#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"} 

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) 

#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

#Add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) 

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) 

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) 

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) 

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 


#Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) 

#Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) 

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) 

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 

#Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) 

#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) 


#Create a frozenset and check its type:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

