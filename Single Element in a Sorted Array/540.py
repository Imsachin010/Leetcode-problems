class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        N2 = N//2
        left=0
        right = N2

        while left< right:
            mid = (left+ right)//2

            if nums[mid*2] == nums[mid*2 +1]:
                left = mid +1
            else:
                right = mid
        return nums[left *2]
