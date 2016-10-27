#coding:utf-8
# 在一个测试类中创建多个测试用例：


class TestClass(object):
    """docstring for TestClass"""
    def test_one(self):
        x = 'this'
        assert "h" in x
        

    def test_two(self):
        x = 'hello'
<<<<<<< HEAD
        assert "hi" == x
=======
        assert "hello" == x
>>>>>>> 8e268cbfe963820cd8b09d8e85534c06fce1fd99


