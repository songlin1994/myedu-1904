import json

# 字典 以 { } 包起来, : 前面是 key ,后面是value ; 多个键值对用 , 分隔开
adict = {'username':'亚索',"password":"123456"}

# 字典是无序的,他没有索引,只能通过key 去访问value, 并且key 不能重复
def dict_sel():
    print(adict['username'])

# 更新字典里面的 value
def dict_updat():
    # 通过key 去 修改value
    adict['username']='ysl'
    print(adict)

# 删除字典里面的键值对
def dict_del():
    adict.pop('username')
    print(adict)

# 增加字典里面的键值对
def dict_add():
    # 如果key 在原本的字典中不存在,则会新加一个键值对
    adict['age'] = 25
    print(adict)
    bdict = {'list':[1,2,3],'tuple':(4,5)}
    # 合并方式一:  将bdict 添加进 adict
    adict.update(bdict)
    print(adict)

    # 合并方式二: 将 adict 和 bdict 合并,新生成一个dict
    cdict = {"password":"77777",'class':'1904'}
    # 注意第二个字典参数前 要加 **
    ddict = dict(adict, **cdict)
    print(ddict)

# 字典和字符串的转换
def dict_zhuanhuan():
    print(type(adict))
    # json.dumps(adict) 字典 转换成 字符串 , ensure_ascii=False : 防止中文乱码
    str_dict = json.dumps(adict,ensure_ascii=False)
    print(str_dict)
    print(type(str_dict))

    dict_str='{"username": "卡见风使舵","password": "123456"}'
    # json.loads(dict_str)  字符串 转换 成字典
    json_loads = json.loads(dict_str)
    print(type(json_loads))

# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并

if __name__ == '__main__':
    # dict_sel()
    # dict_updat()
    # dict_del()
    # dict_add()
    dict_zhuanhuan()