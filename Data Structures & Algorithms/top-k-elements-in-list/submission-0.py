class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for x, count in freq.items():
            bucket[count].append(x)

        ans = []

        for i in range(len(bucket) - 1, 0, -1):
            for x in bucket[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans

        return ans