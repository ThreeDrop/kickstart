T=int(input())
for tt in range(T):
    N,K=[int(s) for s in input().split()]
    v=[int(s) for s in input().split()]
    if K==0:
        ans=sum(v)/N
    else:
        v.sort(reverse=True)
        
        pre_sum=[v[0]]
        for i in range(1,N):
            pre_sum.append(pre_sum[-1]+v[i])
        dp=[]
        dp.append(pre_sum[-1]/N)
        
        for k in range(1,K+1):
            i=0
            while i<N and v[i]>=dp[-1]:
                i=i+1
            dp.append((dp[-1]*(N-i)+pre_sum[i-1])/N)
        ans=dp[-1]
    print("Case #{}: {}".format(tt+1, ans))   
