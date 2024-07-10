class Solution:
    def maxArea(self, height: List[int]) -> int:
        areas=[]
        l = 0
        r = len(height)-1
        while l < r:
            areas.append((r-l)*(min(height[r], height[l])))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max(areas)
