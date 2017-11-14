# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		char_set = set()
		max_length_so_far = 0
		i = 0
		j = 0
		n = len(s)

		while i < n and j < n:
			if s[j] not in char_set:
				char_set.add(s[j])
				j += 1
				max_length_so_far = max(max_length_so_far, j - i)
			else:
				char_set.remove(s[i])
				i += 1

		return max_length_so_far

if __name__ == '__main__':
	s = Solution()

	s1 = "abcabcbb" #3
	print(s.lengthOfLongestSubstring(s1))

	s1 = "abcabcaz" #4
	print(s.lengthOfLongestSubstring(s1))

	s1 = "a" #1
	print(s.lengthOfLongestSubstring(s1))

	s1 = "" #0
	print(s.lengthOfLongestSubstring(s1))
