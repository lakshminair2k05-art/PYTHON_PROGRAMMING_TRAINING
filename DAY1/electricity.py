
#electricity bill calculator
#first 100 units =1.50/units
# next 100 units=2.50/units
#  above 200 units=4/units calculate bill
#eg; SAMPLE INPUT=75
N=int(input('enter the units consumed'))
if(N<=100 and N>0):
    result=N*1.50
elif(N<=200):
    result=((100)*1.50)+((N-100)*2.50)
else:
    result=((100)*1.50)+((N-100)*2.50)+((N-200)*4)
print(result)