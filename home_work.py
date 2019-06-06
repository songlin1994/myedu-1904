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

# 冒泡排序
def paixu():
    alist=[3,2,1,5,4,9,6,7,8]
    # 外循环 len - 1 :  因为 两两比较 ,比如有10个数 我需要比较 9轮
    # 内循环: len - i -1 : 因为 两两比较 ,比如有10个数 我需要比较 9次, 第二遍的时候 只需要比较 8次,
    # 每一轮都少一次,因为每轮 都会放一个数在后面

    #             if alist[j] > alist[j+1]:     判断相邻两个数 要不要换位置

    #             temp = alist[j]
    #             alist[j] = alist[j+1]     将相邻两个数 换位置
    #             alist[j+1] = temp
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp

    print(alist)

def distenct():
    # list去重
    alist = [3, 2, 1, 5, 4, 4,5]
    blist= []
    for i in alist:
        if i not in blist:
            blist.append(i)
    print(blist)

    # 去重方式 2
    s = set(alist)
    print(s)

if __name__ == '__main__':
    # sum_demo()
    jiujiu()
    # paixu()