class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        lon=0
        for num in s:
            if num-1 not in s:
                le=1
                while num+le in s:
                    le+=1
                lon=max(lon,le)
        return lon            
        