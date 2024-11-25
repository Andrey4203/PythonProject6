board = [
    ['X', 'X', '0'],
    ['0', 'X', '-'],
    ['-', '0', '-']
]


def print_board(board):
    print("  0 1 2")
    print("0", board[0][0], board[0][1], board[0][2])
    print("1", board[1][0], board[1][1], board[1][2])
    print("2", board[2][0], board[2][1], board[2][2])

print_board(board)



def check_winner(board):
    #
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]


    for cord in win_combinations:
        symbols = [board[c[0]][c[1]] for c in cord]

        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True

    return False


def tic_tac_toe():
    print("Добро пожаловать в игру Крестики-нолики!")
    print_board(board)

    current_player = 'X'

    for turn in range(9):
        print(f" Ход игрока {current_player}")


        row = int(input("номер строки: "))
        col = int(input("номер столбца: "))


        if board[row][col] != '-':
            print("Клетка уже занята")
            continue


        board[row][col] = current_player
        print_board(board)


        if check_winner(board):
            print("Игра окончена.")
            return


        current_player = '0' if current_player == 'X' else 'X'

    print("Игра окончена. Ничья!")


