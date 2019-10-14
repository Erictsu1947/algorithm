class Solution:

    def reverse(self, nums, l, h):
        while l < h:
            temp = nums[l]
            nums[l] = nums[h]
            nums[h] = temp

            l += 1
            h -= 1

    def rotate_1(self, nums, k: int) -> None:
        """
        use reverse array
        """
        if len(nums) <= 1:
            return

        length = len(nums)
        l, h = 0, len(nums) - 1
        self.reverse(nums, l, h)

        self.reverse(nums, 0, (k % length) - 1)
        self.reverse(nums, (k % length), len(nums) - 1)

    def rotate(self, nums, k: int) -> None:
        """
        use circle link
        """
        if len(nums) <= 1:
            return

        length = len(nums)
        l, h = 0, len(nums) - 1
        self.reverse(nums, l, h)

        self.reverse(nums, 0, (k % length) - 1)
        self.reverse(nums, (k % length), len(nums) - 1)


