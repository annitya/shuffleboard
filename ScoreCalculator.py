import Puck


class ScoreCalculator:
    table = None

    def __init__(self, table):
        self.table = table
        pass

    def calculate(self, pucks):
        score = 0
        for puck in pucks:
            assert isinstance(puck, Puck.Puck)
            if puck.y > self.table.onePointOffset:
                score += 1
            if puck.y > self.table.twoPointOffset:
                score += 2
            if puck.y > self.table.threePointOffset:
                score += 3
            if puck.y > self.table.fourPointOffset:
                score += 4

        return score
