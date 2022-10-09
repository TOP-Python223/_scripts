
class A:
    attr1 = 'attribute of class A'


class B:
    attr1 = 'attribute of class B'


class C(B, A):
    @classmethod
    def show_attributes(cls):
        for attr in dir(cls):
            if not attr.startswith('__') and not attr.endswith('__'):
                print(attr)


C.show_attributes()
print(C.attr1)
print(C.__mro__)
