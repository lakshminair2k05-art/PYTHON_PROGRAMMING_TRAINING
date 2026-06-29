
T=int(input("Enter the total number of tickets: "))
price=200
cat=0,1
cost=0
if T>15 and cat==1:
    cost=T*price-((20/100)+(5/100))*T*price
elif T>15 and cat==0:
    