from typing import Dict, List

class Communities:

    def __init__(self, graph: Dict[int, Dict[int, float]]):
        self.map: Dict[int, int] = {key:key for key in graph.keys()}
        self.graph: Dict[int, Dict[int, float]] = graph
        self.gates: Dict[int, Dict[int, List[int]]]

    def modularity(self) -> float:
        q = 0.0
        for i in self.map.keys():
            for j in self.map.keys():
                if (Aij := self.graph[i].get(j, 0.0)):
                    q += self.graph[i].get(j, 0.0)
        return q


def louvain_algorithm(
    graph: Dict[int, Dict[int, float]]
) -> Communities:
    communities = Communities(graph)
