print("===== Palindrome Check =====")

text = input("Enter a Word: ")

reverse = text[::-1]

if text.lower() == reverse.lower():
    print("Palindrome")

else:
    print("Not a Palindrome")