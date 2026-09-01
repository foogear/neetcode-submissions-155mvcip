class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if c != stack.pop():
                    return False

        return True