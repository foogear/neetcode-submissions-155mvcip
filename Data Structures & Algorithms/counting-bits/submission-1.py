class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0, 1]

        while len(res) <= n:
            res = res + [x + 1 for x in res]

        return res[0:n + 1]


