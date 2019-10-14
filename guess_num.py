def guess(num, k):
    if num < k:
        return -1
    elif num > k:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n, k):
        """
        :type n: int
        :rtype: int
        """

        l, r = 0, n
        while l <= n:
            mid = (l + r + 1) >> 1
            print(l, mid, n)
            res = guess(mid, k)
            if res == -1:
                l = mid + 1
            elif res == 1:
                r = mid - 1
            else:
                return mid


print(Solution().guessNumber(2, 2))