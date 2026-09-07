class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            if not stack or num[i] > stack[-1]:
                stack.append(num[i])
            else:
                while stack and num[i] < stack[-1] and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(num[i])

        if k > 0:
            del stack[-k:]

        while stack and stack[0] == "0":
            stack.pop(0)

        if not stack:
            return "0"

        return "".join(stack)
