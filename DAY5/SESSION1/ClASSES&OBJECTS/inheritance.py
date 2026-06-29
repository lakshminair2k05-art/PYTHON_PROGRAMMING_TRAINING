
class Dog:
    def sound(self):
        print("BOW BOW")
    def eat(self):
        print("Dog is eating")
class Cat(Dog):
    def sound(self):
        print("Meow Meow")
#Instance

d=Cat()
d.eat()
#@@@@@@@@@@@@@@@@@@2
class Father():
    def eat(self):
        print("Father is eating")
class Son(Father):
    pass
son=Son()
son.eat()
################
class Grandfather:
    def Grandfatherskill(self):
        print("Reading current affairs")


class Father(Grandfather):
    def Fatherskill(self):
        print("Makes money")


class Son(Father):
    def Sonskill(self):
        print("1. Watching reels")
        print("2. Eating")
        print("3. Sleeping")


# object
son = Son()

son.Sonskill()
son.Fatherskill()
son.Grandfatherskill()




    