#global var
ways = 0

def count_steps(n):
    global ways
    print("running counnt ways n: " + str(n) + "ways: " + str(ways))
    #base only one step
    #base 0 steps
    if n < 0:
        pass #do nothing end
    elif n == 0:
        ways += 1
    else:
        #ways += 1
        count_steps(n-1)

        #2 steps
        #ways += 1
        count_steps(n-2)

        #3steps
        if (n-3) >= 0:
            #ways += 1
            count_steps(n-3)

total_steps = 2
count_steps(total_steps)
print(str(ways))
