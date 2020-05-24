T=int(input())
for tt in range(T):
    num=int(input())
    num_str=str(num)
    n=len(num_str)
    min_ans=num
    if num==1:
        min_ans=1
    else:
        if num_str[0]=='1':
            down='8'*(n-1)
            top='2'+'0'*(n-1)
            diff_down=num-int(down)
            diff_top=int(top)-num
            min_ans=min(diff_top,diff_down)
        elif num_str[0]=='9':
            down='8'*n
            top='2'+'0'*n
            diff_down=num-int(down)
            diff_top=int(top)-num
            min_ans=min(diff_top,diff_down)
        else:    
            if n>1:
                for i in range(n):
                    if int(num_str[i])%2!=0:
                        down=num_str[:i]+str(int(num_str[i])-1)+'8'*(n-i-1)
                        diff_down=num-int(down)
                        if int(num_str[i])!=9:
                            top=num_str[:i]+str(int(num_str[i])+1)+'0'*(n-i-1)
                            diff_top=int(top)-num
                            min_ans=min(diff_top,diff_down)
                        else:
                            min_ans=diff_down
                        break
                if min_ans==num:
                    min_ans=0           
            else:
                if num%2==0:
                    min_ans=0
                else:
                    min_ans=1
        
    print("Case #{}: {}".format(tt+1, min_ans)) 
