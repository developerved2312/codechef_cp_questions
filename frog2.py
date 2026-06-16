# https://atcoder.jp/contests/dp/tasks/dp_b
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
# tc = O(N*K)  sc = O(N)
h = list(map(int,input().split()))
dp = [0]*n
for i in range(1,n):
  dp[i] = float('inf')
  for j in range(1,k+1):
    if (i-j)>=0:
      dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
print(dp[n-1])
