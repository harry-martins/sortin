a=int(input())
b=list(map(int,input().split()))
b.sort()
for x in range(0,a):
  print(b[x],end=" ")
