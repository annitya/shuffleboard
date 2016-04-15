import ScoreCalculator


class Table:
    redPucks = None
    greenPucks = None

    onePointOffset = None
    twoPointOffset = None
    threePointOffset = None
    fourPointOffset = None

    edgeOffset = None

    scoreCalculator = None

    def __init__(self, edge_offset):
        self.edgeOffset = edge_offset

        self.redPucks = []
        self.greenPucks = []

        self.onePointOffset = 65
        self.twoPointOffset = 65 + 80
        self.threePointOffset = 65 + 80 + 90
        self.fourPointOffset = 65 + 80 + 90 + 135

        self.scoreCalculator = ScoreCalculator.ScoreCalculator(self)

        pass

    def get_green_score(self):
        return self.scoreCalculator.calculate(self.greenPucks)

    def get_red_score(self):
        return self.scoreCalculator.calculate(self.redPucks)
