def count_bits(num):
    """
    counts the number of one bits in the number and returns the
    number
    """
    str_num = str(bin(num))
    count = 0
    #remove the 0b in python
    str_num = str_num[2:]
    for let in str_num:
        if let == "1":
            count += 1

    return count

def print_binary_nums(num):
    """
    given a binary number print the next smallest and largest number
    with the same # of 1 bits
    """
    #find out # of bits in num
    num_bits = count_bits(num)
    print("num: " + str(num_bits))
    found_match = False
    small_num = (num - 1)
    large_num = (num + 1)

    #loop up and down counting bits until find a match
    while not found_match and small_num > 0:
        if num_bits == count_bits(small_num):
            found_match = True
            print(small_num)
        else:
            small_num -= 1
    if small_num < 1:
        print("small number does not exist")

    found_match = False

    while not found_match and large_num > 0:
        if num_bits == count_bits(large_num):
            found_match = True
            print(large_num)
        else:
            large_num += 1

num = 15
print_binary_nums(num)
