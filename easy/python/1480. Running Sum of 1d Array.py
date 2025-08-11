class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        my_array = []
        num_ant = 0
        for i in nums:         
            my_array.append(num_ant + i)
            num_ant = num_ant+i
        return my_array

#num_ant :0, 1, 
#i: 1, 2
#miarray: [1, 3, ]
#nums: [1,2,3,4]