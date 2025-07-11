# Last updated: 7/11/2025, 5:38:13 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # oposite directions
            # stack[-1] is traveling to the right and asteroid is traveling to the left (negative)
            while stack and stack[-1] > 0 and asteroid < 0:
                # There's going to be a collision, so we check who is bigger
                if abs(stack[-1]) > abs(asteroid):
                    # incoming asteroid died
                    break
                elif abs(stack[-1]) == abs(asteroid):
                    # they both explode
                    stack.pop()
                    break
                else:
                    # old asteroid died  we take next one
                    stack.pop()
            else:
                # they were on the same direction so... just add it
                stack.append(asteroid)

        return stack
