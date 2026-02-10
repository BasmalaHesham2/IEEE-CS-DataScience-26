if __name__=="__main__":
    str=input("enter string\n")
    cnt=0
    str.lower()
    for i in str:
        if i=='e' or i=='i' or i=='a' or i=='u' or i=='o':
            cnt+=1
    print(cnt)