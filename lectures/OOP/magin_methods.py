a = 'str'
b = 'string'
if a in b:
    print('True1')
if b.__contains__(a):
    print('True')

c = 4
d = 3

e = c + d
f = c.__add__(d)

print(dir(d))

class Area:
    def __call__(self, a, b, c):
        p = (a + b + c / 2)
        return p



area = Area()
print(area(3, 2, 1))