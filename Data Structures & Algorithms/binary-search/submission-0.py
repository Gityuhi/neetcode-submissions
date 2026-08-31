class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            harf = (l + r) // 2 
            if nums[harf] > target:
                r = harf - 1
            elif nums[harf] < target:
                l = harf + 1
            else:
                return harf
        return -1
