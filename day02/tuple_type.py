# 新建一个元组类型
atuple = (1,2,3,4)

# 与list的区别 : 只能被访问,不能删除,增加,更改里面的元素

if __name__ == '__main__':
    print(atuple[0])
    print(atuple[0:3])

    # 不能被更改,所以报黄
    atuple[0]=5