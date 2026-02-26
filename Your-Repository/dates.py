#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name) 

#Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")

#Save this code in the file mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 

#Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a) 

#Create an alias for mymodule called mx:
import mymodule as mx
a = mx.person1["age"]
print(a) 

#Import and use the platform module:
import platform
x = platform.system()
print(x) 

#List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x) 


#Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x) 

#Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) 


#Create a date object:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x) 


#Display the name of the month:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) 

