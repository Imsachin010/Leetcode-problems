class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {c: index for index, c in enumerate(order)}

        def greaterThan(w1, w2):
            if w1==w2:
                return False
            
            for c1,c2 in zip(w1, w2):
                if ordering[c1] == ordering[c2]:
                    continue

                elif ordering[c1]> ordering[c2]:
                    return True
                else:
                    return False

            return len(w1) >len(w2)
        
        for w1, w2 in zip(words, words[1:]):
            if greaterThan(w1,w2):
                return False
        return True