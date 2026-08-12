class Solution:
    def largestelement(self,nums):
        largest = nums[0]
        for i in nums:
            if i > largest:
                largest = i
        return largest
obj = Solution()
nums = [35,46,32,45]           
nums2 = [23,21,234,1]

print("The largest Element in Array",obj.largestelement(nums),obj.largestelement(nums2))