class column:
    pieces = ()

    def __init__(self, pieces = ()):
        self.pieces = pieces

    def __str__(self):
        return str(self.pieces)

    def __eq__(self, other):
        return self.pieces == other.pieces
    
    def last(self):
        if self.pieces:
            return self.pieces[-1]
        return None
    
    def is_full(self):
        return self.pieces and len(self.pieces) >= board.ROWS
    
    def poppable(self, player):
        return self.pieces and self.pieces[-1] == player

    def drop(self, player):
        if not self.is_full():
            return column((player,) + self.pieces)
    
    def pop(self, player):
        if self.pieces and self.pieces[-1] == player:
            return column(self.pieces[:-1])

class board:
    COLUMNS = 7
    ROWS = 6
    columns = dict()

    def __init__(self, positions: list = None):
        if positions is None:
            self.columns = {i: column() for i in range(self.COLUMNS)}
        else:
            self.columns = {i: p for i, p in enumerate(positions)}

    @classmethod
    def from_string(cls, string: str):
        rows = string.split("\n")
        cols = [column() for _ in range(cls.COLUMNS)]
        for r in range(cls.ROWS - 1, 0, -1):
            i = 0
            for s in rows[r].strip():
                if s in ("X", "O"):
                    cols[i] = cols[i].drop(s)
                i += 1
        return cls(positions=cols)

    def __str__(self):
        s = ""
        for c in self.columns.keys():
            s += str(c) + " : " + str(self.columns[c]) + "\n"
        return s
    
    def copy(self):
        new_brd = board()
        new_brd.columns = self.columns.copy()
        return new_brd

    def make_drop(self, column, player):
        new_col = self.columns[column].drop(player)
        new_brd = self.copy()
        new_brd.columns[column] = new_col
        return new_brd

    def make_pop(self, column, player):
        new_col = self.columns[column].pop(player)
        new_brd = self.copy()
        new_brd.columns[column] = new_col
        return new_brd

    def is_win(self, player):
        return False
    
    def possible_moves(self, player):
        pos = {"drop": [], "pop": []}

        for num in self.columns.keys():
            if not self.columns[num].is_full():
                pos["drop"].append(num)
            if self.columns[num].poppable(player):
                pos["pop"].append(num)

        return pos