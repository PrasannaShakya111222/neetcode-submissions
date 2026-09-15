class Solution:
    def dailyTemperatures(self, temperatures):
        result =[0]*len(temperatures)
        stack =[]

        for i, temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev=stack.pop()
                result[prev]=i-prev
            stack.append(i)
        return result