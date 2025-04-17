file = "day1/input.txt"
lists = list(map(int, open(file, encoding="utf-8").read().strip().split()))
list_left = [lists[idx] for idx in range(len(lists)) if idx % 2 == 0]
list_right = [lists[idx] for idx in range(len(lists)) if idx % 2 == 1]

# sort lists
list_left.sort()
list_right.sort()

# subtract each term in list_left from each term in list_right
list_diff = [abs(i - j) for i, j in zip(list_left, list_right)]
print(sum(list_diff))