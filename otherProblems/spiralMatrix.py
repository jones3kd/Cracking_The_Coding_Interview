
"""
from pramp technical interviews
Matrix Spiral Print

Given a 2D array (matrix) named M, print all items of M in a spiral order,
clockwise.
For example:

M  =  1   2   3   4   5
      6   7   8   9  10
      11  12  13  14  15
      16  17  18  19  20

The clockwise spiral print is:  1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9
14 13 12
"""
def print_right_side(array, startrow, endrow, startcol, endcol):
    """"print the row and right col"""
    row = startrow
    col = startcol
    while row <= startrow: #print row
        while col <= endcol:
            print(array[row][col]),
            col += 1
        row += 1

    row = startrow + 1
    while row <= endrow:
        print(array[row][endcol]),
        row += 1

def print_left_side(array, startrow, endrow, startcol, endcol):
    """Print backwards bottom row and left col"""
    row = endrow
    col = endcol

    while row >= endrow:
        while col >= startcol:
            print(array[row][col]),
            col -= 1
        row -= 1

    row = endrow - 1
    while row >= startrow:
        print(array[row][startcol]),
        row -= 1

def print_spiral_matrix(array):
    cont = True

    #delete
    num = 0
    startrow = 0
    endrow = len(array) - 1
    startcol = 0
    endcol = len(array[startcol]) - 1
    while(cont):
        print_right_side(array, startrow, endrow, startcol, endcol)

        #setup bottom left side
        startrow += 1
        #same endrow
        #same startcol
        endcol -= 1

        print_left_side(array, startrow, endrow, startcol, endcol)

        if startrow == endrow:
            cont = False #printed whole matrix
        else:
            #same startrow
            endrow -= 1
            startcol += 1
            #same endcol

        num += 1


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array = []
num = 0

for row in range(4):
    array.append([])
    for col in range(5):
        array[row].append(nums[num])
        num += 1

print(array)

print_spiral_matrix(array)
