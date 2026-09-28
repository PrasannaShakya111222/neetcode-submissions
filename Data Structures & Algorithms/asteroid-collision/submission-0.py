class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            destroyed = False
            # Collision happens only when:
            # right-moving asteroid + left-moving asteroid
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    # Stack asteroid explodes
                    stack.pop()

                elif abs(stack[-1]) == abs(asteroid):
                    # Both explode
                    stack.pop()
                    destroyed = True
                    break
                else:
                    # Current asteroid explodes
                    destroyed = True
                    break
            if not destroyed:
                stack.append(asteroid)
        return stack