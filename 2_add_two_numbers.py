# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		start_of_list = ListNode(0)
		curr_result_node = start_of_list
		carry = 0

		while l1 or l2:
			sum = carry
			if l1:
				sum += l1.val
				l1 = l1.next
			if l2:
				sum += l2.val
				l2 = l2.next

			# python 3 // is floor division
			carry, sum = sum // 10, sum % 10
			curr_result_node.next = ListNode(sum)
			curr_result_node = curr_result_node.next

		# handle case when no more digits but still carry
		if carry == 1:
			curr_result_node.next = ListNode(1)

		return start_of_list.next

if __name__ == '__main__':
	s = Solution()

	a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
	b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
	result = s.addTwoNumbers(a, b)
	print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

	a, a.next = ListNode(6), ListNode(6)
	b, b.next = ListNode(6), ListNode(6)
	result = s.addTwoNumbers(a, b)
	print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

	a = ListNode(0)
	b, b.next = ListNode(6), ListNode(6)
	result = s.addTwoNumbers(a, b)
	print("{0} -> {1}".format(result.val, result.next.val))

	a = ListNode(0)
	b = ListNode(0)
	result = s.addTwoNumbers(a, b)
	print("{0}".format(result.val))

