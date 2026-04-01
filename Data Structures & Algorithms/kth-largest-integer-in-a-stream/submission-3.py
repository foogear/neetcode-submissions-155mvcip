class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k-1
        nums.sort(reverse=True)
        self.nums = nums
        return 

    def add(self, val: int) -> int:
        if len(self.nums) <= self.target:
            self.nums.append(val)
            self.nums.sort(reverse=True)
            return self.nums[-1]
        if val > self.nums[self.target]:
            self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.target]
        