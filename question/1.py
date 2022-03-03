num = int(input("Type a number: "))

def fibonacci(num):
    count = 0
    n1 = 0
    n2 = 1
    while num != count:
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
        count += 1

fibonacci(num)