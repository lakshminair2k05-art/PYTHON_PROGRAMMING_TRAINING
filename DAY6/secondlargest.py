
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
l=[a,b,c]
if(a>=b and a>=c)or(a<=b and a<=c):
    print("The second largest number is: ",b)
elif(b>=a and b>=c)or(b<=a and b<=c):
    print("The second largest number is: ",a)
else:
    print("The second largest number is: ",c)   