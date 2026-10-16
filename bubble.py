def use(*args):
    # print(type(args))
    print("Tuple=",args)
    # print("sum=",sum(args))
    # print("max=",max(args))
    # print("min",min(args))
    args= list(args)
    #calculating sum

    sum = 0
    for i in args:
        sum=sum+i
    print("sum=",sum)

    #calculating min

    for i in range(1,len(args)):
        if args[0]>args[i]:
            args[0],args[i] = args[i],args[0]
    print("min:",args[0])

    #calculating max

    for i in range(1,len(args)):
            if args[0]<args[i]:
                args[0],args[i] = args[i],args[0]
    print("max:",args[0])


use(45,34,45,32,2,4,5,6,8)