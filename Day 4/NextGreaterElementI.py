class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        d = {}

        d[nums2[-1]] = -1
        stack.append(nums2[-1])

        for i in range(len(nums2)-2, -1, -1):

            if nums2[i] < stack[-1]:
                d[nums2[i]] = stack[-1]
                stack.append(nums2[i])
                continue

            while stack and nums2[i] > stack[-1]:
                stack.pop()

            if not stack:
                d[nums2[i]] = -1
            else:
                d[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]

        return nums1