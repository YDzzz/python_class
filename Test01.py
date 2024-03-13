"""
60个人从左到右报数，报数为4、5、6的向后转，最后剩下多少人面向老师
"""

num = 60
back = 0


for i in range(num):
    if i % 5 == 0:
        back = back + 1
        continue
    elif i % 6 == 0:
        back = back + 1
        continue
    elif i % 4 == 0:
        back = back + 1
        continue

print(num-back)
