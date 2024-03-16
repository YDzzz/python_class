import random
import string

random.seed(10)

for i in range(10):
    print(chr(random.randint(65, 90)), end="")

print("\n", "".join(random.sample(string.ascii_letters, 4)))


print(int("8"*70) * int("6"*100))

# 使用 槽 进行格式化输出
year = 2024
month = 3
day = 13
print("{}year,{}month,{}day".format(year, month, day))

# 输出反向字符串
print(input("Please input a string:")[::-1])

# 输出15长度的字符串
print("{:=^15.15}".format(input()))
print("{:=^15}".format(input()[0: 15]))
