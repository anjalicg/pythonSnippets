
"""http://python-history.blogspot.com/2010/06/method-resolution-order.html
    when looking up a method, base classes were searched using a simple depth-first left-to-right scheme. - Python2.2
    If any class was duplicated in this search, all but the last occurrence would be deleted from the MRO list. - Python 2.3
    C3 Linearization algorithm - In later pythons -
"""
class A:
    def __init__(self):
        print("iniit A")
    def test(self):
        print("test from A")
class B(A):
    def __init__(self):
        print("init B")
    def test(self):
        print("test from B")
class C(A):
    def __init__(self):
        print("init C")
    def test(self):
        print("test from C")

class D(B,C):
    def __init__(self):
        print("init from D")
    def test1(self):
        print("test1 from D")

class E(C,A):
    def __init__(self):
        print("init from E")
    def test1(self):
        print("test1 from E")
class F(B,C):
    def __init__(self):
        print("init from F")
    def test(self):
        print("test from F")



d = D()
d.test1()
d.test()

