print("Hello Python!")

if True:
    print("True")
else:
    print("False")

str1 = 'ccq'
print(str1)
print(str1[0:-1])

counter = 100
miles = 100.0
name = "ccq"

print(counter)
print(miles)
print(name)

a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))


def aaa():
    """这是一个字符串"""
    pass


print(aaa.__doc__)

x = 5
xx = 5
print(id(x))
print(id(xx))
print(x is xx)

x += 1
print(id(x))
print(id(xx))
print(x is xx)

x = 1000
xx = 1000
print(id(x))
print(id(xx))
print(x is xx)

tup = (12, 34, 56)
tup2 = ('abc', 'def')
tup3 = tup + tup2

print(tup3)

dic = {'name': 'ccq', 'age': 7, 'class': 'first'}
print("dic['name']:", dic['name'])
print("dic['age']:", dic['age'])
dic['age'] = 11
dic['school'] = 'xxx'
print(dic)
print(len(dic))
print(str(dic))
print(type(dic))

cities = {
    '北京': {
        '朝阳': ['国贸', 'CBD', '天街'],
        '海淀': ['圆明园', '中关村', '北京大学']
    },
    '北京2': {
        '朝阳': ['国贸', 'CBD', '天街'],
        '海淀': ['圆明园', '中关村', '北京大学']
    },
    '北京3': {
        '朝阳': ['国贸', 'CBD', '天街'],
        '海淀': ['圆明园', '中关村', '北京大学']
    }
}
print(cities)
for i in cities['北京']:
    print(i)
for i in cities['北京']['海淀']:
    print(i)

for i in cities.keys():
    print(i + ' [ ', end="")
    for j in cities[i].keys():
        print(j + ' ', end="")
    print('] ')

for i in cities.values():
    print(i)

for letter in "ccq":
    if letter == 'q':
        pass
        print('执行pass块')
    print('当前字母：', letter)
print("Good bye!")

n = 0
sum2 = 0
for n in range(0, 101):
    sum2 += n
print(sum2)

print(sum(range(1, 101)))

list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))
print(next(it))

f = open("d:/foo.txt", "w")
f.write("测试python的写入操作\n测试成功!!")
f.close()

f2 = open("d:/foo.txt", "r")
str1 = f2.read()
print(str1)
f2.close()

f3 = open("d:/foo.txt", "r")
while True:
    str1 = f3.readline()
    print(str1 + "dddddd")
    if str1:
        break
f2.close()


class MyClass:
    i = 12345

    def f(self):
        return 'hello word'


x = MyClass()

print("MyClass 类的属性 i 为:", x.i)
print("MyClass 类的方法 f 输出为:", x.f())


class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i


x = Complex(3.0, 4.5)
print(x.r, x.i)


class Test:
    def prt(s):
        print(s)
        print(s.__class__)


t = Test()
t.prt()


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁" % (self.name, self.age))


p = people("ccq", 10, 30)
p.speak()


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()


def r_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return r_fib(n - 1) + r_fib(n - 2)


# num = int(input("输出第几项"))
num = 10
if num <= 0:
    print("请输入正数")
else:
    for i in range(1, num + 1):
        print(r_fib(i))
