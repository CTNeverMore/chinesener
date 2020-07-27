class Solution(object):
    def __init__(self,nums1, nums2): 
        self.nums1 = nums1
        self.nums2 = nums2
    
    def merge(self):
        
        for i in range(len(self.nums1)):

            temporal_number = self.nums1

            for j in range(len(self.nums2)):

                if temporal_number<= self.nums2[j]:


        
        return nums1


if __name__ == "__main__":
    nums1 = [1,3,4,5,6]
    nums2 = [2,3,4,7,8]
    a = Solution(nums1,nums2)
    print(a.merge())

    