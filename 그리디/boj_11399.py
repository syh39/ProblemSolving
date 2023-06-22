n = int(input())
arr = list(map(int, input().split()))
arr.sort()
tmp = arr[0]
res = tmp
for i in range(1, len(arr)):
  tmp += arr[i]
  res += tmp
print(res)