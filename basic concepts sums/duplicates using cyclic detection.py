# Note:
# This code might not satisfy the space constraint of the problem, but is a very simple code that is plausible to come up with during an interview.
# If your answer is cycle detection during an interview, the interviewer will know for sure that you have seen the solution before.

# Code:

#     def findDuplicate(self, nums):
# 		return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))
# Explanation:
# The idea is that set of the input array does not contain any repetion. This can be better seen by an example:

# nums = [1, 4, 4, 2, 4]
# set(nums) = {1, 2, 4}

# sum(nums) = 15
# sum(set(nums)) = 7

#  (sum(nums) - sum(set(nums))) = 8
# This difference is due to the fact that number 4 is repeated twice in the nums. The number of the repetion can be calculated as:

# (len(nums) - len(set(nums))) = 2
# And we will have the duplicate number as mentioned in the code:

# (sum(nums) - sum(set(nums))) / (len(nums) - len(set(nums))) = 8 / 2 = 4