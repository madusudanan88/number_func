def l_search_last(S,A=[]):
    N=len(A)
    P=int(N/2)
    for i in range(P-1,0,-1):
        if(S==A[i+P]):
            j=i+P
            break
        elif(M==A[i]):
            j=i
    if(((P*2)!=N)and(A[N-1]==S)):
        j=N-1
    return(j+1)