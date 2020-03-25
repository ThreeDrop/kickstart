T=int(input())
for i in range(T):
    n,b=[int(s) for s in input().split(" ")]
    price=[int(s) for s in input().split(" ")]
    
    price.sort()
    ans=0
    for j in range(n):
        if b>=price[j]:
            ans=ans+1
            b=b-price[j]
    print("Case #{}: {}".format(i, ans)) 