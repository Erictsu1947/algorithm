# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表

    def binary_search(self, array, target):
        length = len(array)
        l, h = 0, length - 1
        while l <= h:
            mid = l + (h - l) // 2
            print(l, mid, h)
            if array[mid] < target:
                l = mid + 1
            elif array[mid] > target:
                h = mid - 1
            else:
                return True
        return False

    def Find(self, target, array):
        # write code here
        for sub_array in array:
            if not sub_array:
                continue
            if target < sub_array[0]:
                return False
            exists = self.binary_search(sub_array, target)
            if exists:
                return True
        return False

nums = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
result = Solution().Find(15, nums)
print(result)
