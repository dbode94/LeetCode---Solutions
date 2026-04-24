# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"


# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s):
    capital_vowels_ascii = {65, 69, 73, 79, 85}
    start_pointer = 0
    end_pointer = len(s) - 1
    aux_list = list(s)

    while start_pointer < end_pointer:
        if (ord(aux_list[start_pointer]) in capital_vowels_ascii or ord(aux_list[start_pointer]) - 32 in capital_vowels_ascii) and (ord(aux_list[end_pointer]) in capital_vowels_ascii or ord(aux_list[end_pointer]) - 32 in capital_vowels_ascii):
            temp = aux_list[start_pointer]
            aux_list[start_pointer] = aux_list[end_pointer]
            aux_list[end_pointer] = temp
            start_pointer += 1
            end_pointer -= 1
        elif not (ord(aux_list[start_pointer]) in capital_vowels_ascii or ord(aux_list[start_pointer]) - 32 in capital_vowels_ascii):
            start_pointer += 1
        elif not (ord(aux_list[end_pointer]) in capital_vowels_ascii or ord(aux_list[end_pointer]) - 32 in capital_vowels_ascii):
            end_pointer -= 1

    return ''.join(aux_list)


def main():
    print(reverseVowels('leetcode'))


if __name__ == "__main__":
    main()
