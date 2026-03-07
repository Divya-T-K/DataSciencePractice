class Solution(object):
    def maxVowels(self, s, k):
        vowel = {'a','e','i','o','u'}
        count = 0
        maxi = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        maxi = count
        for i in range(k,len(s)):
            if s[i] in vowel:
                count += 1
            if s[i-k] in vowel:
                count-= 1
            maxi = max(count,maxi)
        return maxi        