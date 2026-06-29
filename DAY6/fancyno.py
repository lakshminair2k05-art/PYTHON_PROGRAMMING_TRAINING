
N=input("Enter a number: ")
inc=True
dec=True
for i in range(len(N)-1):
    #increasing
    if int(N[i+1])!=int(N[i])+1:
        inc=False
    #decreasing
    if int(N[i+1])!=int(N[i])-1:
        dec=False

if inc :
    print("The number is fancy.")
elif dec:
    print("The number is fancy.")
else:
    print("The number is not fancy.")

