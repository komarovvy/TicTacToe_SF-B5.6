player_sign = ('x', 'o')

def show_field():
    print("  0 1 2")
    for n, row in zip(range(3), ttt_field):
        print(n, *row)

def line_is_done():
    return True

def get_move():
    return 0, 0

def change_player(player):
    return 1 - player


print("Hello! Let's play TicTacToe!")
print("Enter row, column coordinates to make a move")

ttt_field = [['-' for c in range(3)] for r in range(3)]
player = 1
# while line_is_done():
#     player = change_player(player)
#     row, col = get_move(player)
#     ttt_field[row, col] = player_sign(player)
#     show_field()
#
# print("Player", player_sign(player), "wins!")

show_field()