class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in arr:
                return [arr[need], i]
            arr[num] = i
        