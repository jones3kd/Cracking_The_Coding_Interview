"""
1.5 CCI

Kelsey Jones
date: 12/13/14
"""

def compress(string):

    new_str = ""
    char_list = []
    org_len = len(string)
    stack = []

    if str is not None and len(string) > 0:

        for char in string:
            if len(stack) == 0 or stack[-1] == char:
                stack.append(char)
            else:
                tup = (stack[-1], len(stack))
                char_list.append(tup)
                stack = []
                stack.append(char)

        tup = (stack[-1], len(stack))
        char_list.append(tup)
        stack = []

        for tup in char_list:
            new_str += tup[0] + str(tup[1])

        if org_len <= len(new_str):
            return string
        else:
            return new_str

    else:
        return string


def main():
    word1 = "aabcccccaaa"
    word2 = ""
    word3 = "aabbcc"
    word4 = "AsssssSSSSAAAA"

    list1 = [word1, word2, word3, word4]

    for test in list1:
        print(test + "  " + compress(test))


if  __name__ == "__main__":
    main()
