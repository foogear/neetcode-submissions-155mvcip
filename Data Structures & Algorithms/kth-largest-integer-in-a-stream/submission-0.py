class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.target = k
        nums.sort(reverse=True)
        self.nums = nums
        return 

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.target-1]
        