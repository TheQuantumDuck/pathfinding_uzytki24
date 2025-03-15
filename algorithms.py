import bisect
from collections import defaultdict
from typing import Any, Callable, Dict, List, Tuple


class A_star():

    def __init__(
        self,
        data_transform: Callable[[Any], Any],
        get_neighbours: Callable[[int, Any], Dict[int, float]],
        heurestic: Callable[[int, int, Any], float],
        data: Any
    ):
        self.data = data_transform(data)
        self.get_neighbours = get_neighbours
        self.heurestic = heurestic

    def __call__(self, startNode: int, endNode: int) -> List[Tuple[int, float]]:
        came_from = {}
        g_score, f_score = defaultdict(lambda: float("inf")), defaultdict(lambda: float("inf"))
        g_score[startNode], f_score[startNode] = 0.0, self.heurestic(startNode, startNode, self.data)
        open_set = [(f_score[startNode], startNode)]
        open_set_nodes = set((startNode,))
        while bool(open_set):
            current = open_set[0][1]
            if current == endNode:
                path = [current]
                while current != startNode:
                    current = came_from[current]
                    path.insert(0, current)
                return path
            open_set = open_set[1:]
            open_set_nodes.remove(current)
            for neighbour, dist in self.get_neighbours(current, self.data).items():
                tentative_g_score = g_score[current] + dist
                if tentative_g_score < g_score[neighbour]:
                    came_from[neighbour] = current
                    g_score[neighbour] = tentative_g_score
                    neighbour_f_score = tentative_g_score + self.heurestic(startNode, neighbour, self.data)
                    f_score[neighbour] = neighbour_f_score
                    if neighbour not in open_set_nodes:
                        bisect.insort(open_set, (neighbour_f_score, neighbour))
                        open_set_nodes.add(neighbour)