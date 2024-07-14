def is_happy(num): # num is the number to check if it is happy
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def count_happy_numbers(a, b):
    
    count = 0
    for num in range(a, b + 1):
        if is_happy(num):
            count += 1
    return count
    
str1 = input()
a, b = str1.split(' ')
a = int(a)
b = int(b)
happy_count=count_happy_numbers(a,b)
print(happy_count)
