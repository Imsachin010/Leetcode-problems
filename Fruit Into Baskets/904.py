class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        best = 0
        count = collections.Counter()

        left = 0
        for right in range(N):
            count[fruits[right]] += 1

            while len(count) >= 3:
                count [fruits[left]] -=1
            
                if count[fruits[left]] ==0:
                    del count[fruits[left]]
                left +=1

            best = max(best, right - left +1)
        return best