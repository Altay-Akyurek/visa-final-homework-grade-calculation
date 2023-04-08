def ortalama(a,b,c):
    reply=((a*(0.4))+(b*0.1)+(c*0.5))
    if (c<50):
        print("note %s"%(reply))
        print("you stayed")
    elif (reply<50):
        print("note %s"%(reply))
        print("you stayed")
    else:
        print("note %s"%(reply))
        print("you passed ")
    


while True:
    a=int(input("visa note:"))
    b=int(input("homeword grade"))
    c=int(input("final grade"))
    ortalama(a,b,c)
    



