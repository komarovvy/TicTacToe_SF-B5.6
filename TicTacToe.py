PLAYER_SIGN = ('x', 'o')
ATTEMPT_MAX = 3

def show_field():
    print("  0 1 2")
    for n, row in zip(range(3), ttt_field):
        print(n, *row)

def line_is_done():
    return True

def get_move():
    attempt_count = 0
    while attempt_count < ATTEMPT_MAX:
        row, col = tuple(map(int, (input("Enter row and column numbers (example: 1 2):").split())))
        if all([0 <= row < 3, 0 <= col < 3, ttt_field[row][col] == '-']):
            return (row, col)
        if not all([0 <= row < 3, 0 <= col < 3]):
            print("Row and column numbers should be in 0..2 range!")
        if ttt_field[row][col] != '-':
            print(f"Field {row},{col} is already filled!")
    print(f"Your choise {row},{col}")
    return row, col

def set_field(coord, player):
    if coord[1]:
        ttt_field[coord[0]][coord[1]] = PLAYER_SIGN[player]
        return True
    else:
        return False

def change_player(player):
    return 1 - player


print("Hello! Let's play TicTacToe!")
print("Enter row, column coordinates to make a move")

ttt_field = [['-' for c in range(3)] for r in range(3)]
player = 1
while line_is_done():
    player = change_player(player)
    if not set_field(get_move(), player):
        break
    show_field()
else:
    print("Player '", PLAYER_SIGN(player), "' wins!")


