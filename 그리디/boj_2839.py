n = int(input())
cnt = 0
while n>=3:
  if n % 5 == 0:
    cnt += n//5
    n = 0
  else:
    n -= 3
    cnt += 1

if n == 0:
  print(cnt)
else:
  print(-1)
  