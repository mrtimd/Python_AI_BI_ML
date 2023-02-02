def my_function(food):
  for x in food:
    print(x)

fruits = input("enter fruit")

my_function(fruits)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

n = str(input("Enter name: "))
a = int(input("Enter age: "))

p1 = Person(n, a)

print(p1.name)
print(p1.age)

# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line
 
print("geeks", end =" space")
print("geeksforgeeks")
 
# array
a = [1, 2, 3, 4]
 
# printing a element in same
# line
for i in range(4):
    print(a[i], end =" ")