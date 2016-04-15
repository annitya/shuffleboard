class ScoreCalculator:
    table = None

    def __init__(self, table):
        self.table = table
        pass

    def calculate(self, pucks):
        totalscore = 0
        for puck in pucks:
            position = puck.y - puck.radius
            score = 1

            if self.within(position, self.table.onePointOffset, self.table.twoPointOffset):
                score = 2
            if self.within(position, self.table.twoPointOffset, self.table.threePointOffset):
                score = 3
            if self.within(position, self.table.threePointOffset, self.table.fourPointOffset):
                score = 4
            if position > self.table.fourPointOffset:
                score = 0

            totalscore += score

        return totalscore

    @staticmethod
    def within(y1, start, end):
        return start < y1 < end
        pass
