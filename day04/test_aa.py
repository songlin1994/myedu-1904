import allure
import pytest
from day04 import read_excel

excel_list = read_excel.read_excel_list('./day04/test.xlsx')
ids_list = []
for i in range(len(excel_list)):
    ids_pop = excel_list[i].pop()
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