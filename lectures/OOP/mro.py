# class A:
#     pass
#     # def process(self):
#     #     print('A process()')
#
#
# class B:
#     pass
#     # def process(self):
#     #     print('B process()')
#
#
# class C(B, A):
#     def process(self):
#         print('C process()')
#
#
# obj = C()
# obj.process()
# print(C.mro())

class A:
    pass
    # def process(self):
    #     print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    pass
    # def process(self):
    #     print('C process()')


class D(C, B):
    pass


obj = D()
obj.process()
print(D.mro())
