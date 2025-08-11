# LeetCode Problem 9: Palindrome Number
# Problem: https://leetcode.com/problems/palindrome-number/
class Solution:
   def isPalindrome(self, x: int) -> bool:
    cadena = str(x)
    if cadena == ''.join(reversed(cadena)):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
