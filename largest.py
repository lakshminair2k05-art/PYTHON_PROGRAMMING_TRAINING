
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourth number: "))
if a>=b and a>=c and a>=d:
    print("The largest number is: ",a)
elif b>=c and b>=d:
    print("The largest number is: ",b)
elif c>=d:
    print("The largest number is: ",c)
else:
    print("The largest number is: ",d)