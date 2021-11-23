number = 1
amount_of_zeros = 0
a = int(input())
b = int(input())+1

if a == 0:
    a = 1
for f in range(1, a+1):
    number *=f
print(number)
print(number*101)
print(number*102*101)