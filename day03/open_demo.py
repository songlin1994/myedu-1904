
def open_write():

    # open(文件地址文件名, 打开方式)
    # w+ : 写入时覆盖原有内容
    text_io = open('C:/Users/YSL/PycharmProjects/myedu-1904/day03/test.text', 'w+')
    for i in range(5):
        text_io.write('哈哈哈121312\n')


def open_write1():
    # open(文件地址文件名, 打开方式)
    # a+ : 写入时追加内容
    text_io = open('test.text', 'a+')
    for i in range(5):
        text_io.write('哈哈哈\n')

def open_read():
    text_io = open('test.text', 'r')

    # 读取所有行 ,返回一个list
    # print(text_io.readlines())

    # readline() 读取一行
    print(text_io.readline())
    print(text_io.readlines())


if __name__ == '__main__':
    # open_write1()
    open_read()
    # open_write()