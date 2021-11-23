number = 1
amount_of_zeros = 0
a = int(input())
b = int(input())+1

if a == 0:
    a = 1

for f in range(1, a):
    number *=f

for i in range(a, b):
    number *= i
    number_as_string = str(number)
    for l in range(len(number_as_string)):
        if number_as_string[-1] == '0':
            amount_of_zeros += b-i
            number_as_string = number_as_string[:-1]
        else:
            number = int(number_as_string[-1])
            continue
print(amount_of_zeros)


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
            number = int(str(number)[-1])
            continue
print(amount_of_zeros)
