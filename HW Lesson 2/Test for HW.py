
# list2 = usrList[::2]
# list3 = usrList[1::2]
# list4 = list2 + list3
# print(list2)
# print(list3)
# print(list4)

str = '123456789'
str3 = int(str)
# print(type(str3))
# print(str3)
#
# str2 = str[1]+str[0]+str[2:9]
# print(str2)
for i in str:
    n = int(i) + 100
    print(n)


a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))







