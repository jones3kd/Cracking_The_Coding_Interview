
def insert_bits(N, M, i, j):
    #clear bits between j and i
    range = (j-i) + 1

    base = (2 ** range) - 1 # create binary number with all 1s

    #print(str(base) + " " + bin(base))
    base = (base << i) #move over to adjust to start

    #flip_opp = (2 **((range + i))) - 1
    flip_opp = 0xFFFFFFFF
    #lip_opp = ctypes.c_uint32(flip_opp).value
    #flip_opp = np.int32(flip_opp)
    #base = np.int32(base)
    #print("flip_opp "+bin(flip_opp))
    #print(bin(0xFFFFFFFF))
    base = base ^ flip_opp #flip range numners numbers so they are 0 instead of 1
    #print("after base " + bin(base))
    base = base & int("0xFFFFFFFF", 16)
    #print(bin(base))
    #print("original n:" + bin(N))

    N = N & base

    #print(bin(N))
    M = M << i

    #print(bin(M))
    N = N + M

    #print(bin(N))

    return N



#test cases
#N = 0b10000000000
N = 0b10001111111
M = 0b10011
i = 2
j = 6

print(bin(insert_bits(N, M, i,j)))
