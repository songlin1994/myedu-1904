# 这就是一个列表的数据类型,英文 是 list, 也叫 数组

alist = ['是打发',2,'你好',6,7,1,3]

# 访问list
def list_sel():
    # 通过索引访问 顺序取值: 从0开始数
    print(alist[0])

    # 访问倒数第三位 ,# 倒序取值: 从 -1 开始数
    print(alist[-3])

    # 通过切片访问, 语法: 前索引值 : 后索引值  取的时候取到后索引值的前一位
    print(alist[2:3])

    # 访问 从第五个开始到后面的所有
    print(alist[4:])

    # 不填值的话  从第一个开始取值
    print(alist[:4])

# 删除list中的元素
def list_del():
    # 调用删除方法 不填参数 默认删除最后一位
    alist.pop()
    print(alist)
    # 调用删除方法, 填写参数: 索引值   就可以删除指定元素; 并把删除的元素返回回来,赋值给a
    a=alist.pop(3)
    print(alist)
    print(a)

# 增加list中的元素
def list_add():
    blist = [1,2,3,'4']
    # 增加元素 ,增加在末尾
    blist.append('5')
    print(blist)


    clist = [4,5,6]
    # 合并两个list 中的元素
    blist.extend(clist)
    print(blist)

def list_update():
    qlist = [1,2,6,4,5]
    # 更新列表中的元素 , 根据索引进行更新,值写在= 后面 就可以了
    qlist[0] = 100
    print(qlist)

    # 更新第三位 ,改为200
    qlist[2] = 200
    print(qlist)

def list_order_by():
    qlist = [1, 2, 6, 4, 5]
    # 从小到大排序
    qlist.sort()
    print(qlist)
    # 从大到小排序 # 指定参数入参: reverse=True
    qlist.sort(reverse=True)
    print(qlist)

def list_distinct():
    vlist = [1,2,2,6,6,4,5]
    # set(vlist) : 使用set 方法对 list进行去重,去重后不是list类型,用list() 方法 将这个数据转换成list类型
    vlist = list(set(vlist))
    print(vlist)

    # len(): 获取列表的长度,有几个元素 就 返回几
    print(len(vlist))

# 题: 新建一个list变量,里面有五个元素,访问索引2,切片访问索引1到4,删除索引3,添加两个元素,第0位元素改成字符5,获取索引长度
def home_work():
    alist = [1,2,3,4,5]
    print(alist[2])
    print(alist[1:4])
    alist.pop(3)
    alist.append(6)
    alist.append(7)
    # blist = [6,7]
    # alist.extend(blist)
    alist[0]='5'
    print(len(alist))
    print(alist)

if __name__ == '__main__':
    # list_del()
    # list_add()
    # list_update()
    # list_order_by()
    # list_distinct()
    home_work()
    # qlist = [1, 2, 6, 4, 5]
    # qlist.reverse()
    # print(qlist)