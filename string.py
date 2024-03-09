# coding=utf-8
#string process function

print("len('1234') = ", len("1234"))
print("str(1.2345) = ", str(1.2345))
print("str([1,2]) = ", str([1,2]))

print("hex(425) = ", hex(425))
print("oct(425) = ", oct(425))

'''
    chr()       >>      将Unicode码转化为字符
    ord()       >>      将字符转化为Unicode码
'''

for i in range(12):
    print (chr(i + 9800), end = "")