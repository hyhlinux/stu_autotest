# -*- coding:utf-8 -*-
<<<<<<< HEAD

=======
>>>>>>> 8e268cbfe963820cd8b09d8e85534c06fce1fd99
import pytest
import os


def test_main():
    assert 5 != 5

if __name__ == '__main__':
    # pytest.main()
<<<<<<< HEAD
    # pytest.main("-q test_main.py")   # 指定测试文件
    os.chdir('.')
    targetpath = os.getcwd()
    print(targetpath)
    pytest.main(targetpath)             # 指定测试目录
=======
    pytest.main("-q test_main.py")   # 指定测试文件
    # os.chdir('.')
    # targetpath = os.getcwd()
    # print(targetpath)
    # pytest.main(targetpath)             # 指定测试目录
>>>>>>> 8e268cbfe963820cd8b09d8e85534c06fce1fd99
