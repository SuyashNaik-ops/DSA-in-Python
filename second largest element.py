class solution:
    def slargest(self,nums):
        largest = nums[0]
        slargest = None
        for i in nums:
            if i > largest:
                slargest = largest
                largest = i
            elif i < largest and (slargest is None or i > slargest):
                slargest = i
        return slargest
    def ssmallest(self,nums):
        smallest = nums[0]
        ssmallest = None
        for i in nums:
            if i < smallest:
                ssmallest = smallest
                smallest = i
            elif i > smallest and (ssmallest is None or i>ssmallest):
                return ssmallest







obj = solution()
nums1 = [8,8,7,6,5]
nums = [7, 7, 2, 2, 10, 10, 10]
print("Second largest Element is",obj.slargest(nums),obj.ssmallest(nums))
