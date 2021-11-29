import csv

index_found = False
test_index = -1
temp_sum = 0
final_sum = 15000
search = 1
change_point = -1
search2 = 3
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

    for o in range(141):
        index = 50
        for i in range(141):
            if i != change_point:
                while True:
                    search += 1
                    temp_value = table_sorted[index][search]
                    number_of_occurrences = table[index].count(temp_value)
                    for test in range(number_of_occurrences):
                        test_index = table[index].index(temp_value, test_index+1)
                        if test_index in list_of_cities:
                            temp_sum += temp_value
                            index = test_index
                            list_of_cities.remove(index)
                            search = 1
                            index_found = True
                            break
                    test_index = -1
                    if index_found:
                        index_found = False
                        break
                    
       #chyba pripocitat cestu spat do lucenca
       
            else:
                while True:
                    search2 += 1
                    temp_value = table_sorted[index][search2]
                    number_of_occurrences = table[index].count(temp_value)
                    for test in range(number_of_occurrences):
                        test_index = table[index].index(temp_value, test_index+1)
                        if test_index in list_of_cities:
                            temp_sum += temp_value
                            index = test_index
                            list_of_cities.remove(index)
                            search2 = 2
                            index_found = True
                            break
                    test_index = -1
                    if index_found:
                        index_found = False
                        break
        
        if temp_sum < final_sum:
            final_sum = temp_sum
        temp_sum = 0
        change_point += 1
        list_of_cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
                          98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141]
print(final_sum)
