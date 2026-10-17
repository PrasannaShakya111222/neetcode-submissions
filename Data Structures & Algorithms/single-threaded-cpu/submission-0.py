class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        # Sort tasks by enqueue time & keep original index
        sorted_tasks = sorted(
            (enqueue, process, i)
            for i, (enqueue, process) in enumerate(tasks)
        )
        result = []
        heap = []
        time = 0
        i = 0
        while i < n or heap:
            # Jump to next task's enqueue time if CPU is idle
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]
            # Add all tasks available at current time
            while i < n and sorted_tasks[i][0] <= time:
                enqueue, process, index = sorted_tasks[i]
                heapq.heappush(heap, (process, index))
                i += 1
            # Process shortest task; break ties by original index
            process, index = heapq.heappop(heap)
            result.append(index)
            time += process
        return result