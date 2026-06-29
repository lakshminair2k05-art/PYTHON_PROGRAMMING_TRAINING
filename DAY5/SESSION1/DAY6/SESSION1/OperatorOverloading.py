
#INBUILT METHOD
# print(10+20)
# print("Hello"+"Guys")
# print(5*4)
# print("Hi"*4)
class Book:
    def __init__(self,pages):
         self.pages=pages
# MAGIC METHOD
    def __add__(self,other):
         return self.pages+other.pages
b1=Book(200)
b2=Book(300)

   

