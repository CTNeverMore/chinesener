class Solution(object):
    def __init__(self,nums,val): 
        self.nums = nums 
        self.val = val
    
    def removeElement(self):
        i = 0
        for j in range(len(self.nums)):
            if self.nums[j]!= self.val:
                self.nums[i] = self.nums[j]
                i += 1
        return i 
            


