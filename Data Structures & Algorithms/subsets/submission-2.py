class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def powerSub(numsList): # using TREE and reverse the steps
            powSub = [[], [numsList[-1]]]
            for i in range(len(nums) - 2, -1, -1):
                # for j in ps: LOOP
                for j in range(len(powSub)):
                    t = powSub[j].copy()
                    # ps.append(t.append(i)) NG
                    t.append(numsList[i])
                    powSub.append(t)

            return powSub

        return powerSub(nums)





