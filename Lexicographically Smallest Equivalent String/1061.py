class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #union find DS, disjoint union set Ds,Transitive closure
        smallest = {}
        for x in string.ascii_lowercase:
            smallest [x] = x

        def get_smallest(x):
            if smallest[x] !=x:
                smallest[x] = get_smallest(smallest[x])
            return smallest[x]
            
        for a, b, in zip(s1,s2):
            smaller = min(get_smallest(a), get_smallest(b))
            smallest[get_smallest(a)] = smaller
            smallest[get_smallest(b)] = smaller

        a = []
        for  x in baseStr:
            a.append(get_smallest(x))
        return ''.join(a)

        
            