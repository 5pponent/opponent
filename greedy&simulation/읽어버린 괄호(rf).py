arr = input().split('-')

result = 0
result += sum([int(i) for i in arr[0].split('+')])
for i in range(1,len(arr)):
    result -= sum([int(j) for j in arr[i].split('+')])

print(result)