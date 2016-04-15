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
            if self.within(puck.y, self.table.onePointOffset, self.table.twoPointOffset):
                score += 1
            if self.within(puck.y, self.table.twoPointOffset, self.table.threePointOffset):
                score += 2
            if self.within(puck.y, self.table.threePointOffset, self.table.fourPointOffset):
                score += 3
            if self.within(puck.y, self.table.fourPointOffset, 600):  # TODO: Change to actual end of table.
                score += 4

        return score

    @staticmethod
    def within(y1, start, end):
        return start < y1 < end
        pass
