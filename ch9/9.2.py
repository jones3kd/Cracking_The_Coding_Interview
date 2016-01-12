ways = 0

def count_paths(x, y, destx, desty):
    global ways

    #base if at final x and y
    if x == destx and y == desty:
        ways += 1

    else:
        if x < destx:
            count_paths(x + 1, y, destx, desty)

        if y > desty:
            count_paths(x, y-1, destx, desty)


destx = 2
desty = -2

count_paths(0,0, destx, desty)

print(str(ways))
