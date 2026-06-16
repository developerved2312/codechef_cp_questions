#  https://www.codechef.com/problems/ALTARAY
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    subarr = [1]*n
    # reverse traversal
    for i in range(n-2,-1,-1):
        if arr[i]*arr[i+1]<0:
            subarr[i]=subarr[i+1]+1 
        else:
            subarr[i] = 1 
            
    print(*subarr)
    
    
