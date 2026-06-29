
# Default constructor
class Student:
    batch=4#DATA
    def __init__(self,name):#method#Self=keyword
        self.name=name
        print(self.name)
#create the instance/object of class
s1=Student("LAKSHMI")
print(s1.name)