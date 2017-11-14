# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution(object):
    # This solution merges both arrays and then finds the median based on length (even/odd) O(n) runtime
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Join lists together
        joined_nums = []
        i, j = 0, 0

        while i < len(nums1) or j < len(nums2):
            if j == len(nums2):
                joined_nums.extend(nums1[i:])
                break;
            elif i == len(nums1):
                joined_nums.extend(nums2[j:])
                break;

            if nums1[i] <= nums2[j]:
                joined_nums.append(nums1[i])
                i += 1
            else:
                joined_nums.append(nums2[j])
                j += 1

        # Find median
        if len(joined_nums) % 2 == 1: # odd
            return joined_nums[len(joined_nums) // 2]
        else: # even
            tmp = len(joined_nums) // 2 - 1
            return (joined_nums[tmp] + joined_nums[tmp + 1]) / 2

if __name__ == '__main__':
    s = Solution()
    arr1 = [1, 4, 5]
    arr2 = [2, 3]
    print(s.findMedianSortedArrays(arr1, arr2))
    arr1 = [1, 2, 3, 4]
    arr2 = [2, 3]
    print(s.findMedianSortedArrays(arr1, arr2))
    arr1 = [1, 2]
    arr2 = [3, 4]
    print(s.findMedianSortedArrays(arr1, arr2))

