T=int(input())
for tt in range(T):
    L=int(input())
    words=[s for s in input().split()]
    S1,S2,N,A,B,C,D=[s for s in input().split()]
    N=int(N)
    A=int(A)
    B=int(B)
    C=int(C)
    D=int(D)
    ss=[]
    ss.append(S1)
    ss.append(S2)
    xxx=[]
    xxx.append(ord(S1))
    xxx.append(ord(S2))
    for i in range(2,N):
        num=(A*xxx[i-1]+B*xxx[i-2]+C)%D
        xxx.append(num)
        ss.append(chr(97+(num%26)))
    ss=''.join(ss)
    ans = 0
    for ww in words:
        for i in range(N-len(ww)+1):
            sub = ss[i:i+len(ww)]
            if sub[0]==ww[0] and sub[-1]==ww[-1] and (len(ww)<=2 or sorted(ww[1:-1])==sorted(sub[1:-1])):
                ans+=1
                break
    print("Case #{}: {}".format(tt+1, ret))
