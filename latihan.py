from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        positions = [pos for pos, _ in fruits]
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]
        
        def get_sum(left: int, right: int) -> int:
            l = bisect_left(positions, left)
            r = bisect_right(positions, right)
            return prefix[r] - prefix[l]

        res = 0
        # case 1: go left then right
        for x in range(k + 1):
            left = startPos - x
            right = startPos + max(0, k - 2 * x)
            res = max(res, get_sum(left, right))
        
        # case 2: go right then left
        for x in range(k + 1):
            right = startPos + x
            left = startPos - max(0, k - 2 * x)
            res = max(res, get_sum(left, right))

        return res
