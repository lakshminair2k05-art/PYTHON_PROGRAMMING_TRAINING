
products=eval(input('enter the dictionary:'))
choice=input("KEY/PRICE")
def get_value(item):
    return item[1]#1=value, 0=key
if choice=="KEY":
    sorted_dic=dict(sorted(products.items()))
    print("SORTED DICTIONARY=",sorted_dic)
elif choice=="PRICE":
    sorted_dic=dict(sorted(products.items(),key=get_value))
    print(sorted_dic)
else:
    print('invalid choice')

    
