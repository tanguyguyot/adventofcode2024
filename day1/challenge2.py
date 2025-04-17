file = "day1/input.txt"
lists = list(map(int, open(file, encoding="utf-8").read().strip().split()))
list_left = [lists[idx] for idx in range(len(lists)) if idx % 2 == 0]
list_right = [lists[idx] for idx in range(len(lists)) if idx % 2 == 1]

# find similarities
set_list_left = set(list_left)
similarities = {}
for i in set_list_left:
    count = list_right.count(i)
    if count > 0:
        similarities[i] = count

total = 0
for key, value in similarities.items():
    total += key * value
print(total)
    
# 23981443