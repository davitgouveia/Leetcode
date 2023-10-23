class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        sorted_list_reversed = sorted(nums, reverse=True)

        if sorted_list == nums or sorted_list_reversed == nums:
            return True
        else:
            return False 
