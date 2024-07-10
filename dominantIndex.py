class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=nums.index(max(nums))
        l=[i*2 for i in nums if i != max(nums)]
        k=[j for j in l if j>max(nums)]
        if len(k)>0:
            return -1
        if len(k)==0:
            return m
