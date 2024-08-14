# a=10.2

# print(type(a))
#method overloading
class Computer:
     def __init__(self) -> None:
            # print("hello")
            pass
    
     def config(self,name):
        print("welcome",name)

comp1=Computer()
# comp2=Computer()

# Computer.config(comp1)
# Computer.config(comp2)

# comp1.config("hammad")  
# comp1.config("jhsdkf")  

# method overriding

class Book:
     def displayBook(self):
          print("ASOIAF")

class Author(Book):
     def displayBook(self):
          super().displayBook()
          print("GRRM")

# b=Book()
a=Author()
# a.dipslayBook()
# b.dipslayBook()     

a.displayBook()