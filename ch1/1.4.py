"""
CCI 1.4
Replace spaces in string with %20

Author: Kelsey Jones
Date: 12/12/14
"""
def replace(string):

    if " " not in string:
        return string
    else:
        new_string = ""
        prev = None

        for cur_char in string:

            if cur_char != " ":
                if prev is not None and prev == " ":
                    new_string += "%20"

                new_string += cur_char

            prev = cur_char

        if prev == " ":
            new_string += "%20"

        return new_string

def replaceSpaces(string):
    new_string = "%20".join(string.split())

    if string[0] == " ":
        new_string = "%20" + new_string

    if string[len(string) - 1] == " ":
        new_string += "%20"

    return new_string

def main():
    test1 = "Mr John Smith    "
    test2 = "   Kel  4"

    print(replace(test1))
    print(replace(test2))

    print(replaceSpaces(test1))
    print(replaceSpaces(test2))
            

if  __name__ == "__main__":
    main()
