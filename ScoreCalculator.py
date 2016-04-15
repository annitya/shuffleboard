import Puck


class ScoreCalculator:
    greenScore = 0
    redScore = 0
    table = None

    def __init__(self, table):
        self.table = table
        pass

    def calculate(self):
        """:type table: Table.table """
        for greenPuck in self.table.greenPucks:
            assert isinstance(greenPuck, Puck.Puck)
            if greenPuck.y > self.table.onePointOffset:
                self.greenScore += 1
            if greenPuck.y > self.table.twoPointOffset:
                self.greenScore += 2
            if greenPuck.y > self.table.threePointOffset:
                self.greenScore += 3
            if greenPuck.y > self.table.fourPointOffset:
                self.greenScore += 4

        # print self.greenScore

        pass


