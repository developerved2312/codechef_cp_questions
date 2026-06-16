# https://atcoder.jp/contests/dp/tasks/dp_c
import sys 
input = sys.stdin.readline
n = int(input())
a,b,c = map(int,input().split())
for _ in range(n-1):
  na,nb,nc = map(int,input().split())
  newa = na + max(b,c)
  newb = nb + max(a,c)
  newc = nc + max(a,b)
  a,b,c = newa,newb,newc
print(max(a,b,c))
