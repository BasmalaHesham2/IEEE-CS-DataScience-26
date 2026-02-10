def fun(n):
    if(n<=1):
        return n
    return fun(n-1) +fun(n-2)

if __name__=="__main__":
    n =int(input("enter number \n"))
    for i in range(n):
        print(fun(i),end=' ')