# kickstart
practice for kickstart

round A - allocation: 
```Python 
T=int(input())
for i in range(T):
    N,K,P=[int(s) for s in input().split(" ")] 
    beauty=[[int(s) for s in input().split(" ")] for j in range(N)]
    dp=[[0 for ii in range(P+1)] for jj in range(N)]
    pk=min(P,K)
    dp[0][1:pk+1]=[sum(beauty[0][0:k1]) for k1 in range(1,pk+1)]   
    for nn in range(1,N):  
        sum_s=[sum(beauty[nn][0:cc]) for cc in range(K+1)]
        for pp in range(1,min(P,(nn+1)*K)):   
            for xx in range(min(pp,K)+1): 
                dp[nn][pp]=max(dp[nn][pp],sum_s[xx]+dp[nn-1][pp-xx])
                
    print("Case #{}: {}".format(i+1, dp[N-1][P])) 
```   

round A - plates: 
```Python 
T=int(input())
for i in range(T):
    N,K,P=[int(s) for s in input().split(" ")] 
    beauty=[[int(s) for s in input().split(" ")] for j in range(N)]
    dp=[[0 for ii in range(P+1)] for jj in range(N)]
    pk=min(P,K)
    dp[0][1:pk+1]=[sum(beauty[0][0:k1]) for k1 in range(1,pk+1)]   
    for nn in range(1,N):  
        sum_s=[sum(beauty[nn][0:cc]) for cc in range(K+1)]
        for pp in range(1,min(P,(nn+1)*K)):   
        # we should limit pp or we will get TLE for the test set 2 
            for xx in range(min(pp,K)+1): 
                dp[nn][pp]=max(dp[nn][pp],sum_s[xx]+dp[nn-1][pp-xx])
                
    print("Case #{}: {}".format(i+1, dp[N-1][P])) 
    
```
