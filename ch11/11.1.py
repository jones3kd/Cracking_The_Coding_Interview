def sort_arrays(array1, array2):
    #move elements from A to separate array1
    temp1 = []
    for elem in array1:
        if elem is not None:
            temp1.append(elem)
            elem = None

    cur1 = 0
    cur2 = 0
    elem1 = temp1[cur1]
    elem2 = array2[cur2]
    cur = 0

    while elem1 is not None or elem2 is not None:
        if elem2 is not None and elem1 is None:
            #added everything from A already now add everything from B
            array1[cur] = elem2
            cur2 += 1
        elif elem1 is not None and elem2 is None:
            array1[cur] = elem1
            cur1 += 1
        else:
            if elem1 < elem2:
                print(str(cur))
                array1[cur] = elem1
                cur1 += 1
            else:
                array1[cur] = elem2
                cur2 += 1

        print(str(cur))
        print("cur array1"+str(array1))
        cur += 1
        try:
            elem1 = temp1[cur1]
        except IndexError:
            elem1 = None

        try:
            elem2 = array2[cur2]
        except IndexError:
            elem2 = None


arr1 = [5,7,12,33, None, None, None, None, None, None]
arr2 = [1,2,8,10,20,34]

sort_arrays(arr1, arr2)

print(arr1)
