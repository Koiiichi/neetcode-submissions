class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, res, zero = 1, [], 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                continue
            product *= nums[i]
        for i in range(len(nums)):
            if zero > 1:
                res.append(0)
            elif nums[i] == 0 and zero == 1:
                res.append(product)
            elif nums[i] != 0 and zero == 1:
                res.append(0)
            else: 
                res.append(product // nums[i])
            # zero in the rest of the list -> return 0
            # zero not in the rest of the list -> prod / nums[i] -> 0 div s
        return res

        