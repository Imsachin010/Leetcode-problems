class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        edges = collections.defaultdict(list)

        for u,v in roads:
            edges[u].append(v)
            edges[v].append(u)

        def calculate(node, parent):
            total_people = 1
            total_fuel = 0
            for v in edges[node]:
                if v != parent:
                    people, fuel = calculate(v, node)

                    total_people += people
                    total_fuel +=fuel + ((people + seats - 1)// seats)

            return (total_people, total_fuel)
    
        _, f = calculate(0, -1)
        return f