inicial = str(input("Type a String to check if it is a palindrome: ")).strip().upper()
words = inicial.split()
together = ''.join(words)
reverse = together[::-1]

if reverse == together:
    print(True)
else:
    print(False)