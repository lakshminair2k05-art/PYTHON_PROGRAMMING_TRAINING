
name=input("Enter a string: ")
mid=len(name)//2
#name[star:end]
firstpart=name[0:mid]
secondpart=name[mid:]
#reverse
firstpart=name[:mid]
revFirstpart=firstpart[::-1]
revSecondpart=secondpart[::-1]
result=revFirstpart+revSecondpart
print("Reversed string:", result)
