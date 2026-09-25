class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # if lightest and heaviest person can fit in same boat
            if people[left] + people[right] <= limit:
                left += 1
            # heaviest person always gets on boat (alone / with lightest)
            right -= 1
            boats += 1
        return boats