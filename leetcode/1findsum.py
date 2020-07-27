class Solution(object):
    def __init__(self,nums:[int], target:int):
        self.nums = nums
        self.target = target

    def twosumbaoli(self):
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i,j]
        return []
    
    def twoSumdict(self):
        hashmap ={}
        for index, num in enumerate(self.nums):
            another_num = self.target - num 
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index 
        return None

if __name__ =='__main__':
    # a = Solution([2,4,6],8)
    # print(a.twosumbaoli())

    b = Solution([2,4,6],8)
    print(b.twoSumdict())
