def factorial(x):
    f=1
    if((x%2)!=0):
        f=x
        x1=x
        x2=x-1
    else:
        x1=x+1
        x2=x
    f0=int(x2/2)
    for i in range(1,f0+1):
        f=f*i*(x1-i)
    return(f)

def comb(x,y):
    if(y==0):
        return 1
    temp1=x-y
    temp2=x-temp1
    temp3=1
    if((temp2%2)==0):
        temp4=temp1+1
    else:
        temp4=temp1+1
        temp3=temp4
        temp4+=1
    for i in range(temp4,x,2):
        temp3=temp3*i
        temp3=temp3*(i+1)
    return(temp3)
