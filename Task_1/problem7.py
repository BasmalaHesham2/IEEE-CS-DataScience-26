if __name__=="__main__":
    str = input("enter sentence \n")
    strans=''
    curstr=''
    ans=0
    cnt=0
    for i in str:
        if(i==' '):
            if(len(curstr)>len(strans)):
                strans=curstr
            curstr=''
        else:
            curstr+=i
    
    if(len(curstr)>len(strans)):
        strans=curstr
    print(strans)
