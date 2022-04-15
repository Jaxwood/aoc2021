class Die:
    def __init__(self):
        self.face = 1
        self.rolls = 0

    def roll(self) -> int:
        self.rolls += 1
        die = self.face
        self.face = 1 if self.face == 100 else self.face + 1
        return die


class Player:
    def __init__(self, position: int):
        self.position = position
        self.points = 0

    def move(self, die: int) -> None:
        self.position = 10 if (self.position +
                               die) % 10 == 0 else (self.position + die) % 10

        if self.position > 10 or self.position <= 0:
            raise Exception("Player is out of bounds")

    def score(self):
        self.points += self.position


def part1(player1_position: int, player2_position: int) -> int:
    """play a game of Dirac dice"""
    player1 = Player(player1_position)
    player2 = Player(player2_position)
    die = Die()
    while player1.points < 1000 and player2.points < 1000:
        for _ in range(3):
            player1.move(die.roll())
        player1.score()

        if player1.points >= 1000:
            break

        for _ in range(3):
            player2.move(die.roll())
        player2.score()

    return player2.points * die.rolls if player1.points >= 1000 else player1.points * die.rolls