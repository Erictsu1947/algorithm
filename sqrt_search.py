class Solution:
    def mySqrt(self, x: int) -> int:

        l, h = 0, (x // 2 + 1)

        while l < h:
            mid = (l + h + 1) >> 1
            square = mid * mid
            if square > x:
                h = mid - 1
            else:
                l = mid
        return l

print(Solution().mySqrt(9))