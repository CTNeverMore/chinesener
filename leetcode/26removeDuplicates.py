class Solution(object):
    def __init__(self,nums): 
        self.nums = nums 
    
    def removeDuplicates(self):
        a = 0
        b = 1
        while b < len(self.nums):
            if self.nums[b] == self.nums[a]:
                b += 1
            else:
                a += 1
                self.nums[a] = self.nums[b]
        return a+1

if __name__ == '__main__':
    test = Solution([0,0,1,1,1,2,2,3,3,4])
    print(test.removeDuplicates())