"""
author: Kelsey Jones
CCI 1.1
"""

def hasUniqueChar(sentence):

    dic = {}
    words = sentence.split()

    for word in words:
        for char in word:
            if char not in dic:
                dic[char] = 1
            else:
                return False

    return True

def main():
    wrong = "Apples are yummy"
    right = "ABC SDEF"

    print(hasUniqueChar(wrong))
    print(hasUniqueChar(right))

    print(hasUniqueChar("ASDERFDSFDS"))

if __name__ == "__main__":
    main()
