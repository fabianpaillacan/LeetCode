class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        palabras = s.split()
        ultima = palabras[-1]
        return len(ultima)
      