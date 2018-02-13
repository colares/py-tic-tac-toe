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
    print('   1  2  3')
    print('1 [%s][%s][%s]' % (moves[0][0], moves[0][1], moves[0][2]))
    print('2 [%s][%s][%s]' % (moves[1][0], moves[1][1], moves[1][2]))
    print('3 [%s][%s][%s]' % (moves[2][0], moves[2][1], moves[2][2]))


def make_a_move(symbol):
    xy = input('Column[1,2,3],Row[1,2,3]: ')
    x, y = xy.split(',')
    return {'x': int(x)-1, 'y': int(y)-1, 'symbol': symbol}  #


def in_diag1(x, y):
    return y == x


def in_diag2(x, y, dim):
    return y + x + 1 == dim


def add_move(x, y, symbol, moves):
    # print('add move', y, x, symbol)
    moves[y][x] = symbol
    return moves


def is_valid(move):
    global moves
    dimension = len(moves[0])
    if move['x'] not in range(0, dimension):
        return False
    if move['y'] not in range(0, dimension):
        return False
    if moves[move['y']][move['x']] != ' ':
        return False
    return True


def register_move(move):
    global moves
    dimension = len(moves[0])
    x = move['x']
    y = move['y']
    symbol = move['symbol']
    # print('Next move:', move)
    moves = add_move(x, y, symbol, moves)
    moves = add_move(y, x + dimension, symbol, moves)
    if in_diag1(x, y):
        moves = add_move(x, dimension * 2, symbol, moves)
    if in_diag2(x, y, dimension):
        moves = add_move(x, dimension * 2 + 1, symbol, moves)
    return True


def win(moves, player):
    if [player['symbol']]*len(moves[0]) in moves:
        return True


def tie(moves):
    none = 0
    for l in moves:
        none += l.count(' ')
    return none == 0


def is_ended(moves, players):
    if win(moves, players[0]):
        print(players[0]['symbol'], 'wins!')
        return True
    if win(moves, players[1]):
        print(players[1]['symbol'], 'wins!')
        return True
    if tie(moves):
        print('tie!')
        return True
    return False



moves = init_move_history()
players = init_players()
game_round = 0
invalid_move = False
while not is_ended(moves, players):
    clear()
    # print(moves)
    print_board(moves)
    player = players[game_round % 2]
    print('Player:', player['symbol'])
    if invalid_move:
        invalid_move = False
        print("Invalid move. Try it again", end="")
    print(" ")
    new_move = make_a_move(player['symbol'])
    if not is_valid(new_move):
        invalid_move = True
        continue
    register_move(new_move)
    game_round += 1

