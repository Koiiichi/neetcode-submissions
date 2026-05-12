class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      n = {}
      result = []
      for i in range(len(nums)):
        n[nums[i]] = 1 + n.get(nums[i], 0)
      x = dict(sorted(n.items(), key = lambda item: item[1]))
      y = list(map(list, x.items()))
      for j in range(k):
        result.append(y[(len(y) - 1) - j][0])
      return result
        