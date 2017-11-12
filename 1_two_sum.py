# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
		def twoSum(self, nums, target):
			"""
			:type nums: List[int]
			:type target: int
			:rtype: List[int]
			"""
			num_to_index = {
			# 2:0
			# 7:1
			# ...
			}

			for i, num in enumerate(nums):
				diff = target - num

				if diff in num_to_index:
					return [num_to_index[diff], i]
				else:
					num_to_index[num] = i

if __name__ == '__main__':
	print(Solution().twoSum((2, 7, 11, 15), 9))
	print(Solution().twoSum((2, 2, 3, 4), 4))