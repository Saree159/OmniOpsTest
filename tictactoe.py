# Simple 2-player Tic Tac Toe (terminal)

def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]}")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]}\n")

def winner(b, mark):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(b[i]==b[j]==b[k]==mark for i,j,k in lines)

def full(b):
    return all(s in ("X", "O") for s in b)

def main():
    board = [str(i+1) for i in range(9)]
    current = "X"

    print("Tic Tac Toe — players take turns placing X and O.")
    print("Choose a number (1-9) to mark that cell.")
    print_board(board)

    while True:
        try:
            pos = int(input(f"Player {current}, pick a position (1-9): ")) - 1
            if pos not in range(9):
                print("Please choose a number from 1 to 9.")
                continue
            if board[pos] in ("X", "O"):
                print("That spot is taken. Try another.")
                continue
            board[pos] = current
        except ValueError:
            print("Please type a number.")
            continue

        print_board(board)

        if winner(board, current):
            print(f"🎉 Player {current} wins!")
            break
        if full(board):
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
