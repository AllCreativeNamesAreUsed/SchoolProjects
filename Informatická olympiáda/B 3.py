even_index = []
odd_index = []

answer = 'ano'
a = int(input())
odd_index = list(map(int, input().split()))

for i in range((a + 1)//2):
    even_index.append(odd_index.pop(i))


even_index.sort()
odd_index.sort()


even_index.append(1000000001)
for i in range(a//2):
    if not even_index[i] <= odd_index[i] <= even_index[i + 1]:
        answer = 'nie'

print(answer)