class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        st = []

        # sort each element, then add to dict
        # if already exists after sort, append to the new arr

        # ["cat", "stop", "stop", "cat", "stop", "hat"]
        # ["cat": 0, "stop": 1, "hat": 2]

        j = 0
        for i in range(len(strs)):
            check = "".join(sorted(strs[i]))
            if check in s:
              st[s[check]].append(strs[i])
            else: 
              s[check] = j # external counter 
              j += 1 
              st.append([strs[i]])
        return st
