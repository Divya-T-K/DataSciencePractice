class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first = strs[0]
        last = strs[-1]
        r = []
        for i in range(len(first)):
            if(first[i]!=last[i]):
                break
            r.append(first[i])  
        return "".join(r)      