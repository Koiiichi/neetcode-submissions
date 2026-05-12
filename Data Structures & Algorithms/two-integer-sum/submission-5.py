class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            arr[nums[i]] = i # [-5, 5]
        for i in range(len(nums)):
            j = target - nums[i] # not right 
            if arr.get(j, None) != None and arr[j] != i: return [i, arr[j]]
        