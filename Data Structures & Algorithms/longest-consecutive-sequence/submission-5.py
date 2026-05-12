class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        #[2, 20, 4, 10, 3, 5] -> set

        # case 1: start of sequence and continues
        # case 2: middle of a sequence
        # case 3: start of sequence and stops 
        
        maximum = 0
        for n in numset:
            if n - 1 not in numset: # start of a sequence
                length = 0 
                while n + length in numset:
                    length += 1
                    if length > maximum:
                        maximum = length
        return maximum

    
        