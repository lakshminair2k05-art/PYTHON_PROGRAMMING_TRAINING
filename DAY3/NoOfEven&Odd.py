
nums=list(map(int,input("Enter numbers : ").split()))#slits no. into spaces and map to integer

even=0
odd=0
for num in  nums:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:", even)
print("Odd numbers:", odd)
