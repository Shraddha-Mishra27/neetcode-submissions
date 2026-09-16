class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for i in range(len(nums)):
            if freq[nums[i]]>len(nums)//2:
                return nums[i]

        