class Solution(object):
    def permute(self, nums):
        result = []
        self.backtrack(nums,result,[])
        return result
    def backtrack(self,nums,result,temp):
        if(len(nums) == len(temp)):
            result.append(list(temp))
        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.backtrack(nums,result,temp)
            temp.pop()
        