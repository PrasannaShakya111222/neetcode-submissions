class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increase frequency
        self.freq[val] += 1
        f = self.freq[val]

        # Update maximum frequency
        self.max_freq = max(self.max_freq, f)

        # Put val into stack for this frequency
        self.group[f].append(val)

    def pop(self) -> int:
        # Get most recent element among elements with max frequency
        val = self.group[self.max_freq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If no elements remain at this frequency, decrease max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()