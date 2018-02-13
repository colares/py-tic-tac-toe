import os


def clear():
    os.system('clear')


def init_move_history():
    return [
        [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '],  # board in rows
        [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '],  # columns
        [' ', ' ', ' '], [' ', ' ', ' ']  # diags
    ]


def init_players():
    return {0: {'symbol': 'x'},
            1: {'symbol': 'o'}}


def print_board(moves):
    print('[%s][%s][%s]' % (moves[0][0], moves[0][1], moves[0][2]))
    print('[%s][%s][%s]' % (moves[1][0], moves[1][1], moves[1][2]))
    print('[%s][%s][%s]' % (moves[2][0], moves[2][1], moves[2][2]))


def make_a_move(symbol):
    x = input('Column (1,2,3):')
    y = input('Row (1,2,3):')
    return {'x': int(x)-1, 'y': int(y)-1, 'symbol': symbol}  #


def in_diag1(x, y):
    return y == x


def in_diag2(x, y, dim):
    return y + x + 1 == dim


def add_move(x, y, symbol, moves):
    print('add move', y, x, symbol)
    moves[y][x] = symbol
    return moves


def register_move(move):
    global moves
    dimension = len(moves[0])
    x = move['x']
    y = move['y']
    symbol = move['symbol']
    print('Next move:', move)
    moves = add_move(x, y, symbol, moves)
    moves = add_move(y, x + dimension, symbol, moves)
    if in_diag1(x, y):
        moves = add_move(x, dimension * 2, symbol, moves)
    if in_diag2(x, y, dimension):
        moves = add_move(x, dimension * 2 + 1, symbol, moves)


def is_ended(moves, game_round):
    # todo check if 'o','o','o' or 'x','x','x' is in it
    print ('all moves:', moves)
    return game_round > 10
    # print(moves.items())


moves = init_move_history()
players = init_players()
game_round = 0

while not is_ended(moves, game_round):
    # clear()
    print(moves)
    player = players[game_round % 2]
    print('player:', player)
    print_board(moves)
    register_move(make_a_move(player['symbol']))
    game_round += 1

# clear()
# print(moves)
# print_board()
# add_move(make_a_move('x'))
#
# clear()
# print(moves)
# print_board()
# add_move(make_a_move('x'))


