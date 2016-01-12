"""
Find the first non repeated element in an array. returns the elem
"""

def find_non_repeat(arr):
    freq = {} # dictionary of how frequest the numbers are
    #using the elem as the key. freq[2] = (True, 3) (appears once, index)
    first_elem = None
    first_elem_index = None

    for num in range(0, len(arr)):
        print(str(freq))
        if arr[num] not in freq:
            #make new place in dictionary
            print(" %d make new"%arr[num])
            freq[arr[num]] = (True, num)
        else:
            freq[arr[num]] = (False, None)

    for key in freq:
        #initiliaze
        print(str(key))
        if freq[key][0] is True:
            if first_elem is None:
                first_elem = key
                first_elem_index = freq[key][1]
            else:
                if first_elem_index > freq[key][1]:
                    #new first elem
                    first_elem = key
                    first_elem_index = freq[key][1]

    return first_elem


arr = [1,1,6,3,2,2,3,3,6,77,43,2,5,77,7]
arr1 = [3,5]

print(str(find_non_repeat(arr)))

assert arr != arr1, "The arrays don't match. %s != %s"%(str(arr),str(arr1))
