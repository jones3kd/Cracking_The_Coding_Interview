def getBit(num, i):
    print("num: "+bin(num) + " pos: "+str(i))
    print("1 << %d = "%i),
    print(bin((1 << i)))
    print(bin(num)+" & "+bin((1 << i))),
    print("= "+bin((num & (1 << i))))

    return ((num & (1 << i)) != 0)

print(getBit(3,2))
