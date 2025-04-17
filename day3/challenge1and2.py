import re

def get_mul_list(text):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, text)
    return matches

def mul_list_to_tuple_list(mul_list):
    mul_tuple_list = []
    for mul in mul_list:
        mul = mul[4:-1]
        mul_tuple = tuple(map(int, mul.split(",")))
        mul_tuple_list.append(mul_tuple)
    return mul_tuple_list

def get_sum(tuple_list):
    sum_mul = 0
    for mul in tuple_list:
        sum_mul += mul[0] * mul[1]
    return sum_mul

def get_mul_and_dos(text):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)
    return matches

def is_mul(mul):
    if mul.startswith("mul"):
        return True
    return False

def is_dont(val):
    if val.startswith("don't"):
        return True
    return False

def is_do(val):
    if val.startswith("do()"):
        return True
    return False

def mul_list_to_tuple_list_with_dos_dont(mul_list):
    mul_tuple_list = []
    do = True
    for mul in mul_list:
        if is_dont(mul):
            do = False
        elif is_do(mul):
            do = True
        elif is_mul(mul) and do:
            mul = mul[4:-1]
            mul_tuple = tuple(map(int, mul.split(",")))
            mul_tuple_list.append(mul_tuple)
    return mul_tuple_list
    
if __name__ == "__main__":
    # Data preparation
    file = "day3/input.txt"
    raw_puzzle = open(file, encoding="utf-8").read().strip()
    
    # PART 1
    
    mul_list = get_mul_list(raw_puzzle)
    mul_tuple_list = mul_list_to_tuple_list(mul_list)
    
    sum_of_mul = get_sum(mul_tuple_list)
    print("Sum for part 1 : ", sum_of_mul)
    # 189600467
    
    # PART 2
    
    get_mul_and_dos_list = get_mul_and_dos(raw_puzzle)
    mul_tuple_list = mul_list_to_tuple_list_with_dos_dont(get_mul_and_dos_list)
    sum_of_mul = get_sum(mul_tuple_list)
    print("Sum for part 2 : ", sum_of_mul)
    # 107069718
    
    