
number=list(map(int,input('Enter the numbers:').split()))
even_number=list(filter(lambda x:x%2==0,number))
odd_number=list(filter(lambda x:x%2!=0,number))
print("even No.",even_number)
print("Odd No.",odd_number)
# numbers=[1,2,3,4,5,6,7,8,9]
#evens=list(filter(lambda x:x%2==0,numbers))
#print(even)
