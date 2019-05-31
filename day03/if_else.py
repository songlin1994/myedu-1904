def if_demo():
    #  根据表达式 决定 a 是 True 还是 False
    a = 3>4
    # a是 True ,所以条件成立 打印 a 是 True ,
    # 如果a是 false  条件不成立 走else 分支 ,打印 a 是 Flase
    if a :
        print('a 是 True')
    else:
        print('a 是 Flase')

def elif_demo():
    a =4
    # = 是赋值 , == 是 判断相等
    if a==1:  # 判断 a是否等与1
        print('a是1')
    elif a==2:    # 判断 a是否等与2
        print('a是2')
    elif a==3:    # 判断 a是否等与3
        print('a是3')
    elif a==4:    # 判断 a是否等与4
        print('a是4')
    else:
        print('a不是1,2,3,4')


if __name__ == '__main__':
    # if_demo()
    elif_demo()