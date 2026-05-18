class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we check for the minority and majority characters

        # decide what character to replace
        # keep replacing until k is exhausted
        res = 0
        freq = {}
        maximum_freq = 0
        l = 0 # left pointer
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maximum_freq = max(maximum_freq, freq[s[r]])

            if (r - l + 1) - maximum_freq > k:
                freq[s[l]] = freq[s[l]] - 1
                l += 1
            res = max(res, r - l + 1)

        return res





