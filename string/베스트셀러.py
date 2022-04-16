li = []; do = []
for _ in range(int(input())):
    s = input()
    if s not in do:
        do.append(s)
    li.append(s)

temp = []; ans = []

for item in do:
    temp.append((item, li.count(item)))
print(max(temp)[1])
for item in temp:
    if item[1] == max(temp)[1]:
        ans.append(item[0])
ans.sort()
print(ans[0])