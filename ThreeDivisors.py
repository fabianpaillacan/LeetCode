class Solution:
    def isThree(self, n: int) -> bool:
        i = 1
        contador = 0
        while i<=n:
            if n%i == 0:
                contador += 1
            i += 1 
        if contador == 3: return True
        else: return False

# Test cases
sol = Solution()
print(sol.isThree(2))  # False
print(sol.isThree(3))  # False
print(sol.isThree(4))  # True