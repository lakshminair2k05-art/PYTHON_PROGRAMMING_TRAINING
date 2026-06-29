
def McCarthy(n):
    if n>100:
        return n-10
    
    return McCarthy(McCarthy(n+11))
n=int(input('enter a no.:'))
print("Number:",McCarthy(n))