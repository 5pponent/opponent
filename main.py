식 = input()

"""
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
"""
"""
60-50+40-20+10
답 : -60
"""