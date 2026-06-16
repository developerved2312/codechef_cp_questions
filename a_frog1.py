# https://atcoder.jp/contests/dp/tasks/dp_a
n = int(input())
h = list(map(int, input().split()))
prev2 = 0
prev1 = abs(h[1] - h[0])
for i in range(2, n):
    curr = min(prev1 + abs(h[i] - h[i - 1]),prev2 + abs(h[i] - h[i - 2]))
    prev2 = prev1
    prev1 = curr
print(prev1)
