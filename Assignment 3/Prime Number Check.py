print("===== Prime Number Check =====")

num = int(input("Enter a Number: "))

if num <= 1:
    print(num, "is NOT a Prime Number.")

else:
    prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a Prime Number.")
    else:
        print(num, "is NOT a Prime Number.")