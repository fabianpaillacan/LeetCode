class Solution:
    def hammingWeight(self, n: int) -> int:
        numero = format(n, 'b')
        return numero.count('1')
