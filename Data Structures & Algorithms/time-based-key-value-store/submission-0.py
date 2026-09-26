class TimeMap:

    def __init__(self):
        # Maps each key to  list [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []              
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""
        
        # Binary search to find largest timestamp_prev <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]  # Found valid candidate
                left = mid + 1           # Search for potentially larger valid timestamp
            else:
                right = mid - 1          # Look in left half  
        return result