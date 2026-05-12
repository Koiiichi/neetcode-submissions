class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, results = [], [], []
        prefix.append(1)
        suffix.append(1)
         
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        for i in range(1, len(nums)):
            suffix.append(suffix[i - 1] * nums[len(nums) - i])
        suffix.reverse()
        for i in range(len(nums)):
            results.append(prefix[i] * suffix[i])
        return results

            # [1, 2, 8, 48] 

            # [48, 48, 24, 6]



        