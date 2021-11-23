n = input()
board = list(map(int, input().split()))
ledder_lengths = sorted(list(set(board) - {-1,0}) ,reverse=True)
list_of_ledders = []
for i in ledder_lengths:
    start = board.index(i)
    list_of_ledders.append([start + 1, i, start + i +1])
print(list_of_ledders)
