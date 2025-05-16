class Solution:
    def findGCD(self, nums: List[int]) -> int:
        numberMin= min(nums)
        numberMax = max(nums)
        n = numberMin

        while n > 0:
            comparar = 0
            if numberMin % n == 0 and numberMax % n == 0: return n
            n -= 1

# Test cases
sol = Solution()
print(sol.findGCD([2,5,6,9,10]))  # 2
print(sol.findGCD([7,14]))  # 7
print(sol.findGCD([3,9,27]))  # 3
print(sol.findGCD([1,2,3,4,5]))  # 1
