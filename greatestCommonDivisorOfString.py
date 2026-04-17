# Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"

# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"

# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"

# Output: ""

# Example 4:

# Input: str1 = "AAAAAB", str2 = "AAA"

# Output: ""​​​​​​​


# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

def odd(numb):
    return True if numb % 2 != 0 else False


def getDivisors(numb):
    divSet = set()
    i = 1

    while i * i <= numb:
        if numb % i == 0:
            divSet.add(i)
            divSet.add(numb//i)
        i += 1

    return divSet


def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: set
    """
    # edge case: one of the string is empty
    if not len(str1) or not len(str2):
        return ''

    # getting the intersection of div lenghts
    common_prossible_div_lenghts = sorted(getDivisors(
        len(str1)) & getDivisors(len(str2)), reverse=True)

    # not sure if this a valid case - double check later
    if not len(common_prossible_div_lenghts):
        return ''

    for value in common_prossible_div_lenghts:
        str1_split = str1.split(str2[0: value])
        str2_split = str2.split(str2[0: value])

        bigger_lenght = len(str1_split) if len(
            str1_split) > len(str2_split) else len(str2_split)

        for pos in range(bigger_lenght):
            if pos < len(str1_split) and str1_split[pos] != '':
                break
            if pos < len(str2_split) and str2_split[pos] != '':
                break
        else:
            return str2[0: value]

    return ''


def main():
    print(gcdOfStrings('ABABABAB', 'ABAB'))


if __name__ == '__main__':
    main()


# If str1 odd then str2 has to be odd, if str1 even then str2 has to be even
