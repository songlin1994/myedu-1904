# 导入其他模块

from day01 import base_type

def def1():
    print('def1')

def def2():
    print('def2')

def def3():
    print('def3')

if __name__ == '__main__':
    # 使用其他模块的方法 : 语法 模块名.方法名()
                            # 指定参数入参, 指定num2 =100 ,指定num1 是 20
    value = base_type.add(num2=100, num1=20)
                            # 默认参数入参, 就是按照参数的顺序入参, 100 是num1, 20 是num2
    value1 = base_type.add(100, 20)

    print(value)

    a = '凄凄切切风雨行'
    # 切片演示
    print(a[4:])
    print(a[1:3])

    # 根据索引取值演示
    print(a[0])
    print(a[-1])

    # 反转
    print(a[::-1])