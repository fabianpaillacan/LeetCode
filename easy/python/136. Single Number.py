class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        else:
            for element in nums:
                cont = nums.count(element)
                if( cont == 1):
                    return element
                