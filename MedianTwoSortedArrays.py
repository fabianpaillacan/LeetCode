class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        
        tamanio = len(temp)

        if tamanio%2 == 0:
            mediana = (temp[tamanio // 2 - 1] + temp[tamanio // 2]) / 2
            return mediana         
        else: 
            mediana = temp[tamanio // 2] 
            return mediana