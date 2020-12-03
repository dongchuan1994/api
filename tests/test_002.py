import pytest,sys,os
p=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from base.my import dc
def test_01():
    assert 2== dc()

def test_02():
    assert 2==3

if __name__ == '__main__':
    for i in sys.path:
        print(i)