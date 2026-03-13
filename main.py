from board import board

def main():
    brd = board()
    print(brd.possible_moves("X"))

    brd = board.from_string(
        """-------
        -------
        -------
        -------
        X--O-XO
        X-OXOXO""")
    print(brd)
    print(brd.possible_moves("X"))

if __name__ == "__main__":
    main()