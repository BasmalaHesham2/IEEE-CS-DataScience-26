if __name__ == '__main__':
    num=int(input())
    listt=[]
    while(num>0):
        name=str(input())
        parts=name.split()
        name=parts[0]
        args=parts[1:]
        match name:
               
            case "insert":
                    i=int(args[0])
                    e=int(args[1])
                    listt.insert(i,e)
            case "print":
                    print(listt)
            case "remove":
                    e=int(args[0])
                    listt.remove(e)
            case "append":
                    e=int(args[0])
                    listt.append(e)
            case "sort":
                    listt.sort()
            case "pop":
                    listt.pop()
            case "reverse":
                    listt.reverse()
            case _:
                    pass
        num-=1

