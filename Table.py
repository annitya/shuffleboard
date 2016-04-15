import ScoreCalculator

class Table:
    redPucks = []
    greenPucks = []

    onePointOffset = None
    twoPointOffset = None
    threePointOffset = None
    fourPointOffset = None

    edgeOffset = None

    scoreCalculator = None

    def __init__(self, edge_offset):
        self.edgeOffset = edge_offset

        self.onePointOffset = 75
        self.twoPointOffset = 150
        self.threePointOffset = 225
        self.fourPointOffset = 300

        self.scoreCalculator = ScoreCalculator.ScoreCalculator(self)

        pass

    def get_score(self):
        self.scoreCalculator.calculate()
        pass
