class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def powerSub(numsList):
            res = [[], [numsList[-1]]]
            for i in range(len(nums) - 2, -1, -1):
                for j in range(len(res)):
                    if len(res[j]) < k:
                        t = res[j].copy()
                        t.append(numsList[i])
                        res.append(t)
            return res

        nums = [x for x in range(1, n + 1)]
        originalList = powerSub(nums)

        res = []
        for l in originalList:
            if len(l) == k:
                res.append(l)

        return res



