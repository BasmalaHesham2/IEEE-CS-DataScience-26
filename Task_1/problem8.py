import math
if __name__=="__main__":
    x1=int(input("enter x1\n"))
    y1 = int(input("enter y1\n"))
    x2=int(input("enter x2\n"))
    y2 = int(input("enter y2\n"))

    x=(abs(x2-x1))
    y=abs(y2-y1)
    x=pow(x,2)
    y=pow(y,2)
    print(math.sqrt(x+y))