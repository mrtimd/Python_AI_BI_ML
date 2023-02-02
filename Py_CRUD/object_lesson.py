class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

MyFather = Person("John", 36)

MyMother = Person("MyMother", 36)

MySister = Person("MySister", 36)

MyBrother = Person("MyBrother", 36)


print(MyFather.name)
print(MyFather.age)

print(MyMother.name)
print(MyMother.age)

print(MySister.name)
print(MySister.age)