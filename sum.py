'''# Get input from the user
n = int(input("Enter a positive number: "))

# Initialize variables
sum_n = 0
i = 1

# Use while loop to calculate sum
while i <= n:
    sum_n += i
    i += 1  # Increment i

# Print the result
print(f"The sum of the first {n} natural numbers is: {sum_n}")'''


#factorial of a number
n = int(input("Enter a number: "))
factorial =1
for i in range(1, n+1):
    factorial *=i
print(f"The factorial of {n} is: {factorial}")
