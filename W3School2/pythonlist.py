mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#-1 refers to the last item, -2 refers to the second last item etc.
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) 

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
Example

Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist 

#The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 

#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 

#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) 

newlist = [x for x in fruits if x != "apple"] 

newlist = [x for x in fruits] 

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5] 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 





