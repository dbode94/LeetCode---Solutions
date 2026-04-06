# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.


# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]


# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104


def findErrorNums(nums):
    numbers = {number+1: 0 for number in range(len(nums))}

    for num in nums:
        numbers[num] = numbers[num] + 1

    numb_sorted = sorted(
        numbers.items(), key=lambda item: item[1], reverse=True)

    return [numb_sorted[0][0], numb_sorted[len(numb_sorted) - 1][0]]


def main():
    nums = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
    print(findErrorNums(nums))


if __name__ == "__main__":
    main()
