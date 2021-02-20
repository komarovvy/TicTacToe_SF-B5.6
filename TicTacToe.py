PLAYER_SIGN = ('x', 'o', '-')
ATTEMPT_MAX = 3
FIELD_SIZE_X = 3
FIELD_SIZE_Y = 3
WIN_LINE_LEN = 3


def show_field(fld):
    print(" ", end='')
    for i in range(len(fld[0])):
        print(f" {i}", end='')
    print("")
    for n, row in zip(range(len(fld)), fld):
        print(n, *row)


def is_win_len(L):
    while len(L) - WIN_LINE_LEN >=0:
        same_len = 1
        char = L.pop()
        if char == PLAYER_SIGN[2]:
            continue
        while L and L[-1] == char:
            same_len += 1
            L.pop()
        if same_len >= WIN_LINE_LEN:
            return True
    return False


def line_is_done(fld):
    col_num = len(fld[0])
    row_num = len(fld)
    # rows check
    for row in range(row_num):
        if is_win_len([fld[row][col] for col in range(col_num)]):
            return True
    # columns check
    for col in range(col_num):
        if is_win_len([fld[row][col] for row in range(row_num)]):
            return True
    #\ diagonal
    for row in range(row_num):
        if is_win_len([fld[row+i][i] for i in range(min(row_num-row, col_num))]):
            return True
    for col in range(1,col_num):
        if is_win_len([fld[i][col+i] for i in range(min(row_num, col_num-col))]):
            return True
    #/ diagonal
    for row in range(row_num):
        if is_win_len([fld[row-i][i] for i in range(min(row+1, col_num))]):
            return True
    for col in range(1,col_num):
        if is_win_len([fld[row_num-1-i][col+i] for i in range(min(row_num, col_num-col))]):
            return True

    return False


def get_move():
    attempt_count = ATTEMPT_MAX + 1
    while attempt_count:
        attempt_count -= 1
        if attempt_count != ATTEMPT_MAX:
            print(f"{attempt_count} attempts left. ", end='')
        row, col = tuple(map(int, (input("Enter row and column numbers (example: 1 2):").split())))
        if not all([0<= row < len(ttt_field), 0 <= col < len(ttt_field[0])]):
            if 0<= row < len(ttt_field):
                print(f"Column number should be in 0..{len(ttt_field[0])-1} range!")
            elif 0 <= col < len(ttt_field[0]):
                print(f"Row number should be in 0..{len(ttt_field)-1} range!")
            else:
                print(f"Row/column number should be in 0..{len(ttt_field)-1}/0..{len(ttt_field[0]-1)} range!")
            continue
        elif ttt_field[row][col] != '-':
            print(f"Field {row},{col} is already filled!")
            continue
        break
    else:
        return None, None

    return row, col


def set_field(fld, coord, player):
    if coord[0] is None:
        return False
    else:
        fld[coord[0]][coord[1]] = PLAYER_SIGN[player]
        return True


def change_player(player):
    return 1 - player


print("Hello! Let's play TicTacToe!")
print("Enter row, column coordinates to make a move")


ttt_field = [[PLAYER_SIGN[2] for c in range(FIELD_SIZE_X)] for r in range(FIELD_SIZE_Y)]
player = 1

show_field(ttt_field)
while not line_is_done(ttt_field):
    player = change_player(player)
    if not set_field(ttt_field, get_move(), player):
        break
    show_field(ttt_field)
else:
    print("Player '", PLAYER_SIGN[player], "' wins!", sep= '')

