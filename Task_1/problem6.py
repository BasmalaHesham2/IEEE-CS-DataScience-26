if __name__=="__main__":
    num=int(input("enter number\n"))
    for i in range(11):
        if((num*i)%4!=0):
            print(num*i,end=' ')