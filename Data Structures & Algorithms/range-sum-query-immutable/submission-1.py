class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        sum = 0
        for n in nums:
            sum += n
            self.nums.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        left = self.nums[left - 1] if left - 1 >= 0 else 0
        return self.nums[right] - left

        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)