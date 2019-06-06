# 导入需要用的模块
import allure
import pytest
from day04 import read_excel

# 调用一下方法 读取excel
excel_list = read_excel.read_excel_list('./day04/test.xlsx')
# 声明一个 list类型变量, 用来存用例名
ids_list = []
# 遍历 excel_list
for i in range(len(excel_list)):
    # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
    ids_pop = excel_list[i].pop()
    # 将ids_pop添加到 ids_list 里面
    ids_list.append(ids_pop)


@allure.feature('测试字符串')
class Test_bb:

    @allure.story('实际测试')
    @pytest.mark.parametrize('astr,msg',
        [['成功', '操作成功'], ['失败', '操作成功'], ['失败', '操作失败']],
        ids= ['测试成功','测试异常','测试失败场景'])
    def test_dd(self,astr,msg):
        assert astr in msg

    @allure.story('实际测试_参数化')
    @pytest.mark.parametrize('astr,msg',excel_list,ids=ids_list)
    def test_cc(self, astr, msg):
        assert astr in msg