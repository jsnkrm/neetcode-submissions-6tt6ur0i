class CountSquares:

    def __init__(self):
        self.points = []
        self.ptsCount = defaultdict(int)
    
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(x - px) != abs(y - py) or x == px or y == py):
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res

