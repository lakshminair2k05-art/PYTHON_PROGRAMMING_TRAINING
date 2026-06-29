price=float(input('Enter the ticket price:'))
NumberofTickets=int(input("enter the no. of tickets:"))
Category=int(input("Enter the category of ticket 1 or 0: "))
discount=0
amount=NumberofTickets*price
if NumberofTickets>15:
    discount +=20
if Category== 1:
    discount += 10
if discount>0:
    amount=amount-(amount*discount/100)
    if NumberofTickets>15 and Category==1:
        print("Discount applied:-1.MaxTicket and 2.Student")
    elif NumberofTickets>15:
        print("Discount applied:-1.MaxTicket")
    else:
        print("Discount applied:-2.Student")
else:
    print("No discount applied")
print("Total amount to be paid: ",amount)
 



