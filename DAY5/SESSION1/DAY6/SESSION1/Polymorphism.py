# I)compile time-1.)Method overloading :same fun name but diff parameter
class Demo:
    #def add(self,a):

        #print(a)
    #def add(self,a,b):
      #  print(a+b)
    def add(self,*numbers):
        print(sum(numbers))
    
obj=Demo()
obj.add(18.9,9,0)
obj.add(10,20)