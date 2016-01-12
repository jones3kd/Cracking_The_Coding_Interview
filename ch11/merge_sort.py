def merge_sort_inner(start, end, arr):
    "Incluse end 0-4 includes 4"
    #if only one element do nothing and return
    if end - start < 1:
        #do nothing
        return
    else:
        #atleast 2 elements in start and end
        #divide halfs
        mid = (end - start / 2)

        merge_sort_inner(start, mid, arr)
        merge_sort_inner(mid+1, end, arr)

        #now merge 2 halfs
        merge(start, mid, mid+1, end, arr)

def merge(start, mid1, mid2, end, arr):
    cur = 0
    cur1 = start
    cur2 = mid2

    s_arr = [None] * (end - start + 1)
    print(s_arr)
    return

def merge_sort(arr):
    #start merge
    merge_sort_inner(0, len(arr) - 1, arr)




arr = [1,8,4,2,99,3,44,5,21,4,5,3]
arr1 = [3, 6]

print(arr1)
merge_sort(arr1)
print(arr1)
