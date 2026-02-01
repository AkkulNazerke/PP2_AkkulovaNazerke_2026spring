print(10 > 9)
print(10 == 9)
print(10 < 9) 
#When you run a condition in an if statement, Python returns True or False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))

#Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))