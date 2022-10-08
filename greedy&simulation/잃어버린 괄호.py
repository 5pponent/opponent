식 = input()
수 = []; 연산자 = []

s = 0
for i in range(len(식)):
    if 식[i] in ['+', '-']:
        수.append(식[s:i])
        연산자.append(식[i])
        s = i + 1
수.append(식[s:])

for i in range(len(수)):
    수[i] = str(수[i]).lstrip('0')

최종식 = ''
for i in range(len(연산자)):
    최종식 += 수[i]
    최종식 += 연산자[i]
최종식 += str(수[len(수)-1])

temp = list(최종식)
idx = 0; cnt = 0
while True:
    if idx > len(temp)-1:
        break
    if temp[idx] == '-':
        cnt += 1
        if cnt % 2 == 1:
            temp.insert(idx+1, '(')
        else:
            temp.insert(idx, ')')
    idx += 1
if cnt > 0 and temp[len(temp)-1] != ')':
    temp.append(')')

최종식 = "".join(str(i) for i in temp)
print(eval(최종식))
