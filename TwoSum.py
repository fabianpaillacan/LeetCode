# Problem: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #nums porque arriba se declara que el nombre de la lista es nums
            for j in range(i+1, len(nums)): #j empieza en i+1 porque no quiero comparar el mismo elemento
                if nums[i] + nums[j] == target: #si la suma de los dos elementos es igual al target devuelvo la posicion de los dos elementos
                    return [i, j]