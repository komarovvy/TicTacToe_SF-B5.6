PLAYER_SIGN = ('x', 'o', '-')
ATTEMPT_MAX = 3
FIELD_SIZE_X = 4
FIELD_SIZE_Y = 5

def show_field(fld):
    print(" ", end='')
    for i in range(len(fld[0])):
        print(f" {i}", end='')
    print("")
    for n, row in zip(range(len(fld)), fld):
        print(n, *row)

def check_eq_val(L):
    return True

def line_is_done():
    # for i in range(;):
    #     check_eq_val(ttt_field[i])
    #     check_eq_val([l for l in ttt_field[0:-1][i]])
    #
    return True

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
    # print(f"Your choise {row},{col}")
    return row, col

def set_field(coord, player):
    if coord[1] is None:
        return False
    else:
        ttt_field[coord[0]][coord[1]] = PLAYER_SIGN[player]
        return True

def change_player(player):
    return 1 - player


print("Hello! Let's play TicTacToe!")
print("Enter row, column coordinates to make a move")

# ttt_field = [[(r+1)*10+c+1 for c in range(FIELD_SIZE_X)] for r in range(FIELD_SIZE_Y)]
ttt_field = [[PLAYER_SIGN[2] for c in range(FIELD_SIZE_X)] for r in range(FIELD_SIZE_Y)]
player = 1
while line_is_done():
    player = change_player(player)
    if not set_field(get_move(), player):
        break
    show_field(ttt_field)
else:
    print("Player '", PLAYER_SIGN(player), "' wins!")

#TODO code line_is_done()

