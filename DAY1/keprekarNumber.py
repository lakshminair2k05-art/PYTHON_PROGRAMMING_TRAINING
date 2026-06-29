
N=int(input('enter the number to check keprekar'))
square=N*N
digits=len(str(N))
right=square%(10**digits)#2025 DIV BY 100 = REMINDER 25
left=square//(10**digits)#2025/100 =20.25 FLOOR DIV=20
if left+right==N:#20+25 =55
    print('Keprekar')
else:
    print('Not Keprekar')
