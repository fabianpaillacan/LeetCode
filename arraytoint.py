class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join(map(str, digits)))
        integer += 1
        return [int(d) for d in str(integer)]

        