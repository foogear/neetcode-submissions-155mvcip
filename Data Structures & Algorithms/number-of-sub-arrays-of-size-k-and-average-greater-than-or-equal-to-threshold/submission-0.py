class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        res , sum, l = 0, 0, 0

        for r in range(len(arr)):
            sum += arr[r]
            if r - l == k - 1:
                if int(sum / k) >= threshold:
                    res += 1
                sum -= arr[l]
                l += 1

        return res


