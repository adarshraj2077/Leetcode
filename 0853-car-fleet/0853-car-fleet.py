# My Approach
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        count = 0

        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack:
                stack.append(time)
                count += 1

            elif time > stack[-1]:
                stack.append(time)
                count += 1

            else:
                continue
        
        return count

# ChatGPT Approach slightly better bcs no need to append stack

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         stack = []
#         cars = sorted(zip(position, speed), reverse=True)

#         for pos, spd in cars:
#             time = (target - pos) / spd

#             if not stack or time > stack[-1]:
#                 stack.append(time)

#         return len(stack)