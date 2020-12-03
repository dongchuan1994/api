import pytest

if __name__ == '__main__':
    path = "--html=.\\report\\测试报告.html"
    pytest.main([path])
    import sys
    for i in sys.path:
        print(i)