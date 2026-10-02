class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Find intersection point of  two pointers in cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Find  "entrance" to cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow