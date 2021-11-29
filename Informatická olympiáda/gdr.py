import csv

temp_sum = 0
final_sum = 15000
list_of_cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
                          98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141]
table_sorted = []

with open('b4.csv', 'r') as file:
    table = list(csv.reader(file))

    for y in range(1, 142):
        for x in range(1, 142):
            table[y][x] = int(table[y][x])

    table_sorted.append(table[0])
    for i in range(1, 142):
        t = table[i][1:142]
        t.sort()
        t.insert(0, table[i][0])
        table_sorted.append(t)
        t.index

print(len(table[141]))
print(len(table_sorted[141]))
print(table_sorted[57][120])
test_index = table[117].index(28)
print(test_index)