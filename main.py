from _typeshed import Self


a = input("Enter a number: ")
b = int(a)

for i in range(b):
    print(" " * (b-i-1) , end=" ")
    print("*" *(i*2+1), end=" ")
    print(" " * (b-i-1))

class Dog(self, name, age):
    self.name = name 
    self.age = age
