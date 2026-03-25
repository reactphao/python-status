"""
模块级 docstring 示例：
用于说明脚本用途或模块说明。
"""

# 单行注释示例：变量赋值

a = 1
a = '10'
print(a)  # 行尾注释示例

print(type(a))

# 单行注释：input 返回的是字符串
input_a = input('请输入一个数字:')
print(type(input_a))
print(input_a)

input_age = input('请输入你的年龄:')
print(type(input_age))
print(input_age)

try:
    # 多行注释示例（常用写法）：使用多个 # 号
    # 这里将字符串转换为 int
    # 如果无法转换，会抛出 ValueError
    input_age = int(input_age)
    if input_age >= 18:
        print('你已经成年了')
    else:
        print('你未成年')
except ValueError:
    print('你输入的年龄不是数字')
    exit()





