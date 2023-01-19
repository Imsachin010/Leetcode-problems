class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lookup = collections.Counter()
        lookup[0] = 1
        current = 0
        an = 0
        for x in nums:
            current += x
            current %= k
            an += lookup[current]
            lookup[current] += 1
        return an