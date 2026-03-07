from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        dq = deque()
        ans = []
        for i in range(n):
            while(dq and dq[0]<=i-k):
                dq.popleft()
            while(dq and nums[i]>nums[dq[-1]]):
                dq.pop()
            dq.append(i)
            if(i>=k-1):
                ans.append(nums[dq[0]])
        return ans