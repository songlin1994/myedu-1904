# 求 1到50之间的奇数和
def sum_demo():
    sum = 0
    for i in range(1, 51):
        if i % 2 == 1:
            sum = sum + i
    print(sum)
# 打印九九乘法表
def jiujiu():

    for i in range(1,10):
        x = i+1
        for j in range(1,x):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
            print()
        print('')
# 求两个数之间的偶数和
def sum_demo1(a,b):
    sum = 0
    if a<b:
        for i in range(a,b):
            if i%2 ==0:
                sum = sum+i
    elif a>b:
        for i in range(b,a):
            if i %2 ==0:
                sum = sum+i
    else:
        print('a和 b 相等')

    print(sum)


if __name__ == '__main__':
    # 顺序入参
    sum_demo1(10,20)
    # 指定参数入参
    sum_demo1(a=10,b=20)
    sum_demo1(b=20,a=10)
    pass
