class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = [-1]*256
        l = 0
        r = 0
        maxi = 0
        while(r<len(s)):
            if(l<=freq[ord(s[r])]):
                l = freq[ord(s[r])]+1
            len1 = r-l+1
            maxi = max(len1,maxi)
            freq[ord(s[r])] = r
            r += 1
        return maxi
        