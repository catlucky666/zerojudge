n=int(input())
h=0
a=list(map(int,input().split()))
if(a[0]==0):
    a[0]=a[1]
    h=h+a[0]
    if(a[n-1]==0):
        a[n-1]=a[n-2]
        h=h+a[n-2]
        for i in range(1,n):
            if(a[i]==0):
                a[i]=min(a[i-1],a[i+1])
                h=h+a[i]
        
    
    elif(a[n-1]!=0):
        for i in range(1,n):
            if(a[i]==0):
                a[i]=min(a[i-1],a[i+1])
                h=h+a[i]
        
        
elif(a[0]!=0):
    if(a[n-1]==0):
        h=h+a[n-2]
        for i in range(n-1):
            if(a[i]==0):
                a[i]=min(a[i-1],a[i+1])
                h=h+a[i]
        
        
    elif(a[n-1]!=0):
        for i in range(n):
            if(a[i]==0):
                a[i]=min(a[i-1],a[i+1])
                h=h+a[i]
        
print(h)