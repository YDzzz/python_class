#string

str1 = "'Hello World'"
str2 = '"Hello World"'
str3 = """
"first line"
    'second line'
        '''third line'''"""
str4 = '''
"first line"
        'second line'
            """third line"""'''

print (str1)
print (str2)
print (str3)
print (str4)

#index
print ("str[1] = ", str1[1])
#slice
print ("str[1: 6] = ", str1[1: 6])
#字符串反转
print ("str[::-1] = ", str1[::-1])

'''
tips：
    使用" "的字符串内部可以随意使用' '
    使用' '的字符串内部可以随意使用" "
    使用""" """的字符串内部不能使用""" """
    使用''' '''的字符串内部不能使用''' '''
'''

'''
转义字符：
    \n      >>      换行
    \"      >>      "
    \b      >>      回退
    \r      >>      回车
'''



