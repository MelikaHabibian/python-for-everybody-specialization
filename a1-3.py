import re
hand = open('regex_sum_1033351.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    lst = re.findall('([0-9]+)', line)
    for num in lst:
        sum = sum + int(num)
print(sum)
