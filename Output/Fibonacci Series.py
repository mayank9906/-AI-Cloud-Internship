print("===== Fibonacci Series =====")

n = int(input("Enter Number of Terms: "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(n):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number