# We need to modify the array in-place and the size of the final array would potentially be smaller than the size of the input array. So, we ought to use a two-pointer approach here. One, that would keep track of the current element in the original array and another one for just the unique elements.
# We keep 2 pointers

# i to keep track of the position to place the next unique element
# j to. traverse the list to find the next unique element
# We return 0 if nothing is in nums otherwise we initialize both i and j to 1 since nums[0] is of course unique and is already in the correct location.

# nums[i-1] will hold the number we just placed and we check nums[j] against it, do nothing if they are the same, otherwise place the element in nums[i] incriment i and j and move on


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1

def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = list(sorted(set(nums)))
        return len(nums)