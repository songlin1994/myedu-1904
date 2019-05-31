# 求 1到50之间的奇数和
def sum_demo():
    sum = 0
    for i in range(1, 51):
        k = i % 2
        if k == 1:
            sum = sum + i
    print(sum)

# 打印九九乘法表
def jiujiu():
    # 因为乘法表里面有两个数,所以写两个for 循环
    # 乘法表 从1到 9  所以外循环是 range(1,10)
    # 内循环 写i+1 因为 每次每一行 数字 j 最大的都是i
    # 内循环打印 就是字符串拼接,以 ' '结尾 防止每次打印换行,并 分隔开每次打印内容
    # 外循环的print 主要是为了 每次内循环结束 需要换行
    for i in range(1,10):

        for j in range(1,i+1):
            print('%s * %s = %s'%(j,i,j*i),end='   ')
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

'''
每次拿 4 个 最后剩一个, 
每次拿五个剩四个,
每次拿6个 最后剩3个,
每次拿七个最后剩5个,
每次拿八个最后剩一个,
每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
'''

# 篮子拿鸡蛋 1
def jidan():
    for i in range(1, 1000):
        if (i % 4 == 1):
            if (i % 5 == 4):
                if (i % 6 == 3):
                    if (i % 7 == 5):
                        if (i % 8 == 1):
                            if (i % 9 == 0):
                                print(i)
# 篮子拿鸡蛋 2
def jidan2():
    for i in range(1, 1000):
        if i%4!=1:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 3:
            continue
        if i % 7 != 5:
            continue
        if i % 8 != 1:
            continue
        if i % 9 != 0:
            continue
        print(i)

if __name__ == '__main__':
    # sum_demo()
    jiujiu()