if __name__=="__main__":
    num=int(input("Enter number\n"))
    strn=str(num)
    n=len(strn)
    finl=0
    for i in strn:
        finl+=pow(int(i),n)
    
    if(finl==num):
        print("YES\n")
    else : print("NO\n")