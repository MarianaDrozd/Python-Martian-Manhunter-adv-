class MyMetaClass1:
    def __init__(self, my_attr = 1):
        self.my_attr_1 = my_attr

print(type(MyMetaClass1))
obj_1 = MyMetaClass1()
print(obj_1.my_attr_1)
print(type(obj_1))

def my_class_init(self, attr_value):
    self.attr = attr_value


MyMetaClass = type('MyMetaClass', (object, ), {'__init__': my_class_init})
print(type(MyMetaClass))
obj = MyMetaClass('test')
# print(type(obj))
print(obj.attr)