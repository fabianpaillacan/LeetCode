class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
     plano = [elemento for fila in matrix for elemento in fila]
     print(plano)
     if target in plano: return True
     else: return False