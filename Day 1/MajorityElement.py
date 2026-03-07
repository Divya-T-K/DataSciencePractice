class Solution(object):
    def majorityElement(self, nums):
        s = None
        c = 0
        for i in nums:
            if c == 0:
                s = i
            c += (1 if i == s else -1)
        return s