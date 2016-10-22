#coding:utf-8
# 在一个测试类中创建多个测试用例：


class TestClass(object):
    """docstring for TestClass"""
    def test_one(self):
        x = 'this'
        assert "h" in x
        

    def test_two(self):
        x = 'hello'
        assert "hi" == x


