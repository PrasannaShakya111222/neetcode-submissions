class Solution:
    def largestRectangleArea(self, heights):
        stack=[]
        max_area=0
        heights.append(0)

        for i, h in enumerate(heights):

            while stack and h<heights[stack[-1]]:
                height=heights[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i

                max_area=max(max_area,height*width)
            stack.append(i)
        heights.pop()
        return max_area