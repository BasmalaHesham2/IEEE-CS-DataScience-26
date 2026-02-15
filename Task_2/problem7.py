if __name__=="__main__":
    f=open("simple_text.txt")
    text=f.read()
    word=text.split()

    cnt=0
    for x in word:
        if(len(x)>5):
            cnt+=1

    print(cnt)
    f.close()