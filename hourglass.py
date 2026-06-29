
N=5
for j in range(N,0,-1):
    print(" "*(N-j),end=" ")
    print("*"*(2*j+1))

for i in range(N):
    print(" "*(N-i-1),end=" ")
    print("*"*(2*i+1))