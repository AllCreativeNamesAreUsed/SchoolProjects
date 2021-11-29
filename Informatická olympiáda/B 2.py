number = 1
amount_of_zeros = 0
a = int(input())
b = int(input())+1

if a == 0:
    a = 1

for f in range(1, a):
    number *= f

for i in range(a, b):
    number *= i

    for l in range(len(str(number))):
        if number % 10 == 0:
            amount_of_zeros += b-i
            number = number // 10
        else:
            continue
print(amount_of_zeros)
