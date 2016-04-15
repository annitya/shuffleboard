import DistanceCalculator


class Table:
    redPucks = []
    greenPucks = []
    distanceCalculator = None
    edgeOffset = None

    def __init__(self, edge_offset):
        self.edgeOffset = edge_offset
        self.distanceCalculator = DistanceCalculator.DistanceCalculator()
        pass

