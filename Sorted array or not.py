class solution:
    def sortedarray(self, nums):
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
        return True


obj = solution()

nums = [1, 2, 3, 4, 5]
nums2 = [32, 12, 4, 24]

print(obj.sortedarray(nums), obj.sortedarray(nums2))