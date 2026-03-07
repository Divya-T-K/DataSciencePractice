class Solution(object):
    def search(self, nums, target):
        l = 0
        h = len(nums) - 1
        while(l<=h):
            mid = (l+h)//2
            if(nums[mid] == target):
                return mid
            if(nums[l]<=nums[mid]):
                if(target>=nums[l] and target<nums[mid]):
                    h = mid-1
                else:
                    l = mid+1
            else:
                if(target<=nums[h] and target>nums[mid]):
                    l = mid + 1
                else:
                    h = mid-1
        return -1