
class A:
    attr1: str = 'test attribute'

    @classmethod
    def show_attributes(cls):
        print(' '.join(
            attr
            for attr in dir(cls)
            if not attr.startswith('__') and not attr.endswith('__')
        ))


class B(A):
    pass


class C(A):
    attr2: float = 0.01


A.show_attributes()

B.show_attributes()
print(B.attr1)

C.show_attributes()
print(C.attr1, C.attr2)
