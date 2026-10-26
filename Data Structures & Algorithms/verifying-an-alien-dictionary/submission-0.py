class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Create mapping of each character to its alien order index
        order_map = {char: idx for idx, char in enumerate(order)}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            # Compare characters of w1 & w2
            for j in range(len(w1)):
                # If w1 runs out of characters, w2 is longer & starts with w1 (correct)
                if j == len(w2):
                    return False
                char1 = w1[j]
                char2 = w2[j]
                if char1 != char2:
                    # If w1's character comes after w2's character in alien order (invalid)
                    if order_map[char1] > order_map[char2]:
                        return False
                    # If w1's character comes before w2's character, this pair is valid; (stop checking)
                    break
        return True