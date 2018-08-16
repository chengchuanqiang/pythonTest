a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

a = 0
b = 1
while b < 1000000:
    print(b, end=',')
    n = a + b
    a = b
    b = n
print()
i = 256 * 256
print('i 的值为:', i)

print(a, b, sep='@')


def fab(n):
    if n < 1:
        print('输入有误！')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


print(fab(26))

fabArr = [0, 1, 1]
print(fabArr[0])
print(fabArr[1])
print(fabArr[2])
n = 26
for i in range(3, n + 1):
    fabArr.append(fabArr[i - 1] + fabArr[i - 2])
print(fabArr[n])
