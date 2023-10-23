class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        final = []
        for x in range(len(nums)):
            if ((nums[x] % 2) == 0):
                final.insert(0,nums[x])
            else:
                final.append(nums[x])
        
        return final
