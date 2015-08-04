"""
CCI 1.3
Check if 2 stirngs are permutations of each other

Author: Kelsey Jones
Date: 12/12/14
"""

def is_permutation(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) == len(word2):
        str1 = {}
        str2 = {}

        for num in range(len(word1)):
            cur_let1 = word1[num]
            cur_let2 = word2[num]

            if cur_let1 not in str1:
                str1[cur_let1] = 1
            else:
                str1[cur_let1] += 1

            if cur_let2 not in str2:
                str2[cur_let2] = 1
            else:
                str2[cur_let2] += 1

        for key in str1:
            if not (key in str2 and str2[key] == str1[key]):
                return False
            
        return True
            
    else:
        return False

def is_permutation2(word1, word2):

    if len(word1) == len(word2):
        return sorted(word1) == sorted(word2)
    else:
        return False

def main():
    word1 = "leey"
    word2 = "yek"

    word3 = "abc"
    word4 = "bac"

    print(is_permutation(word1, word2))
    print(is_permutation(word3, word4))

    print(is_permutation2(word1, word2))
    print(is_permutation2(word3, word4))

if  __name__ == "__main__":
    main()
