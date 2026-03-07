class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        h = len(nums) - 1
        while(l<=h):
            mid = (l+h)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid]<target):
                l = mid+1
            else:
                h = mid - 1
        return l