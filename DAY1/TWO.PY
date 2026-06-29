
#Vehicle=200;Wheel=540;tw=130;fw=70 NO. OF TWO WHEELERS AND FOUR WHEELERS IN A MALL OF 200 VEHICLES

tv=int(input("Enter the total number of vehicles: "))
tw=int(input("Enter the number of two wheels: "))
y=(tw-2*tv)//2
x=tv-y
print("The number of two wheelers is: ",x)
print("The number of four wheelers is: ",y)