num = int(input('Type a number: '))
total = 0
for i in range (1, num + 1):
    if num % i == 0:
        total += 1
if total == 2:
    print(f'The number {num} is prime')
else: 
    print(f'The number {num} is not prime')