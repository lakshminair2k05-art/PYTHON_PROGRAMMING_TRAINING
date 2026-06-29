N = 6

for i in range(N//2, N, 2):
    print(" "*(N-i) + "*"*i + " "*(N-i) + "*"*i)

for i in range(N, 0, -1):
    print(" "*(N-i) + "*"*(2*i-1))
