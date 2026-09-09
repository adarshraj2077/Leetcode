class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0 and ast < 0 and stack[-1] < abs(ast):
                    stack.pop()

                if not stack:
                    stack.append(ast)

                elif stack[-1] == abs(ast) and stack[-1] > 0 and ast < 0:
                    stack.pop()

                elif stack[-1] > abs(ast) and stack[-1] > 0 and ast < 0:
                    pass

                else:
                    stack.append(ast)

        return stack