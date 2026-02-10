if __name__=="__main__":
    num1=int(input("enter first num \n"))
    num2=int(input("enter sec num\n"))
    op=input("enter operation\n")
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    else: print(num1/num2)

