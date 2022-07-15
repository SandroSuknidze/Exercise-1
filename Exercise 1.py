list1 = []
for _ in range(int(input())):
    inp = input()
    while inp == '':
        inp = input()
    list1.append(inp)


mylist = set(list1)
print(len(mylist))


res = {}
for val in list1:
    if val in res:
        res[val] += 1
    else:
        res[val] = 1

for value in res.values():
    print(value, end=" ")