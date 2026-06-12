# cook your dish here
t = int(input())

for _ in range(t):
    m,x,y = map(int,input().split())
    
    cops = list(map(int,input().split()))
    safe = [True]*101
    distance = x*y
    
    for house in cops:
        left = max(1,house-distance)
        right = min(100,house+distance)
        
        for i in range(left,right+1):
            safe[i] = False
            
    count = 0 
    for i in range(1,101):
        if safe[i]:
            count = count+1
    print(count)
