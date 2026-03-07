class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in map:
                return [map[c],i]
            map[nums[i]] = i