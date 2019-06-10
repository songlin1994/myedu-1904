
# 声明一个类  语法:  class 类名(父类名):
class Human(object):
    # __init__ : 类的初始化方法
    # self : 代表类的本身 ,name,age,sex 初始化的时候 要用到的参数
    def __init__(self,name,age,sex):
        # self.name = name : 把方法中的参数 绑定给 类的属性
        self.name = name
        self.age = age
        self.sex = sex

    # 类中的方法 必须包含self 参数
    def eat(self):
        print(self.name+'在吃饭 ')

    def sleep(self):
        print(self.name+'在睡觉')

    # 类中的方法,可以调用其他方法,可以调用属性,除了init 方法
    def info(self):
        print('这个人叫%s,今年%s岁,性别: %s'%(self.name,self.age,self.sex))
        self.eat()

# 继承 : 继承那个类 就写那个类
# 继承之后 子类 拥有父类中的属性 和  方法
class Tester(Human):

    def __init__(self, name, age, sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job

    #  如果 子类中的方法名 和 父类中的重复了 , 那么这个叫重写方法, 调用时 调用子类中的方法
    def eat(self):
        print(self.name+'在吃工作餐')

    def do_test(self):
        print(self.name+'在做测试')
        self.sleep()

if __name__ == '__main__':
    # 新建一个对象 , 根据 Human 类 新建对象
    # 对象是 类的 实例化
    # girl = Human('田雨', 18, '女')
    # 可以通过对象去调用类的方法和属性
    # girl.eat()
    # girl.sleep()
    # girl.info()
    # print(girl.name)


    tester = Tester('咸鱼', 25, '男','资深测试工程师')
    tester.do_test()
    tester.eat()
