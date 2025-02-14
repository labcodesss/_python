n = 4

for i in range(4):
    print("*"*(i+1))

'''n=3
for i in range(3):
    print(" " *(n-i-1),end ="")
    print("*" *(2*i+1),end ="")
    print(" " *(2*i+1))'''

n = 3  # Number of rows

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


n = 3  # Number of rows

for i in range(n):
    if i == 0 or i == n - 1:
        print("***")  # First and last row full of stars
    else:
        print("* *")  # Middle row with spaces in between




