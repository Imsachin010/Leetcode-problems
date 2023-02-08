class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        INF = 10**20

        farthest =0
        distance = 0
        i = 0
        while True:
            if farthest >= N-1:
                return distance
            
            new_far = 0
            while i <N and  i <= farthest:
                new_far = max(new_far, nums[i] +i)
                i +=1
            farthest = new_far
            distance +=1