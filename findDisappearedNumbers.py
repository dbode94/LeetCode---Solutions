# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]


# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n


# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# first solution
# def findDisappearedNumbers(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     sorted_nums = sorted(nums)
#     missing_nums = []

#     for i, num in enumerate(sorted_nums):
#         if i+1 != num:
#             missing_nums.append(i+1)

#         if num in missing_nums:
#             missing_nums.remove(num)

#     return missing_nums

# def findDisappearedNumbers(nums):
#     return [i for i in range(1, len(nums)+1) if i not in nums]


def findDisappearedNumbers(nums):
    sorted_nums = sorted(nums)
    missing_nums = []

    if sorted_nums[0] != 1:
        missing_nums += range(1, sorted_nums[0])

    for i, num in enumerate(sorted_nums):
        if i > 0 and num - sorted_nums[i - 1] > 1:
            missing_nums += range(sorted_nums[i - 1] + 1, num)

    if sorted_nums[len(sorted_nums) - 1] != len(sorted_nums):
        missing_nums += range(sorted_nums[len(sorted_nums) -
                              1] + 1, len(sorted_nums) + 1)

    return missing_nums


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))


if __name__ == "__main__":
    main()
