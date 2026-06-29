
tuple_list=eval(input("Enter list of tuples : "))
k=int(input("Enter the coloumn index k: "))
product=1
for tup in tuple_list:
    product=product*tup[k]
        
print(f"product of values:{k}:{product}")