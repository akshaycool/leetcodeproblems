class Solution(object):
    
    # def recFindNonDup(self,nums):
    #     print "nums",nums
    #     if len(nums) == 1:
    #         return nums[-1]
    #     n = len(nums)
    #     l = self.recFindNonDup(nums[:n/2])
    #     r = self.recFindNonDup(nums[n/2:])
    #     print l
    #     print r
    #     if not l:
    #         return r
    #     if not r:
    #         return l
    
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # #Method1 - Non-logn
        # if n == 1:
        #     return nums[-1]
        # for i in range(0,n-1,2):
        #     if nums[i]!=nums[i+1]:
        #         return nums[i]
        # return nums[-1]
        
        #Method2 - Binary search - logn
        l,r = 0,n-1
        mid = l + (r - l)/2
        while l < r:
            mid = l + (r - l)/2
            if mid%2:
                if nums[mid] == nums[mid-1]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[mid] == nums[mid+1]:
                    l = mid+2
                else:
                    r = mid
        return nums[l]
        
        #return self.recFindNonDup(nums)