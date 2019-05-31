def jisuan(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)   # 10 / 8 : 商 是 1 余 2
    print(a % b)    # 取余

# 比较符 完成后 会返回一个bool值 ,只有True 和 False
def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)  # == : 判断相等
    print(a <= c)
    print(a >= b)  # 大于等于
    print(a != b)  # 不等于

#自增 , 自减
def deng(a):
    a+=1 # a =a+1  这就是自增
    print(a)

    a-=1 # a = a-1  自减
    print(a)

    a*=3
    print(a)

    a/=9
    print(a)

if __name__ == '__main__':
    # deng(9)
    jisuan(10,3)