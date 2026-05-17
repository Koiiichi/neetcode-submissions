class Solution:
    def isValid(self, s: str) -> bool:
        track = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                track.append(c)
            else:
                if not track:
                    return False

                if c == ')' and track[-1] == '(':
                    track.pop()
                elif c == '}' and track[-1] == '{':
                    track.pop()
                elif c == ']' and track[-1] == '[':
                    track.pop()
                else:
                    return False

        return not track