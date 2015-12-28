"""
Determine the # of bits required to convert
It A into Int B
"""

def count_bits(num):
    #counts bits, 1s in number
    str_num = str(bin(num))
    #take out leading 0b
    str_num = str_num[2:]
    count = 0

    for let in str_num:
        if let == '1':
            count += 1

    return count


def get_bits_convert(num1, num2):
    rs_num = num1 ^ num2

    return count_bits(rs_num)

num1 = 35
num2 = 12

rs = get_bits_convert(num1, num2)

print(rs)
