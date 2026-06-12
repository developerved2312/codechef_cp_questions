# little elephant and candies
t = int(input())

for _ in range(t):
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    print("Yes" if sum(a) <= c else "No")
