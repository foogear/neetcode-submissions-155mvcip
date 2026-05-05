class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        l, res = 0, 1
        prev, curr = None, None
        # a = [arr[0]]

        for r in range(1, len(arr)):
            if arr[r] > arr[r - 1]:
                curr = "<"
            elif arr[r] < arr[r - 1]:
                curr = ">"
            else:
                curr = "="

            if curr != prev and curr != "=":
                # print(curr)
                # a.append(arr[r])
                prev = curr
            elif curr == prev:
                # for _ in range(r - l - 1):
                #    del a[0]
                l = r - 1
                # a.append(arr[r])
            elif curr == "=":
                l = r
                # a = [arr[l]]
            
            res = max(res, r - l + 1)
            # print(a)

        return res



            