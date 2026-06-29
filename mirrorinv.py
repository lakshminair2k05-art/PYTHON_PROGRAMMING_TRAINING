
N = 5

# Top half of butterfly
for i in range(1, N + 1):
    print('*' * i + ' ' * (2 * (N - i)) + '*' * i)

# Bottom half of butterfly
for i in range(N, 0, -1):
    print('*' * i + ' ' * (2 * (N - i)) + '*' * i)