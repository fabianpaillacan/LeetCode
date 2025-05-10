# LeetCode Problem 9: Palindrome Number
# Problem: https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10 + (x % 10)
            x = x // 10     
        return original == reversed_num