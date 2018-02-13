import os


def clear():
    os.system('clear')


def init_move_history():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def init_players():
    return {0: {'symbol': 'x'},
            1: {'symbol': 'o'}}


def print_board(moves):
    print('[%s][%s][%s]' % (moves[0][0], moves[1][0], moves[2][0]))
    print('[%s][%s][%s]' % (moves[0][1], moves[1][1], moves[2][1]))
    print('[%s][%s][%s]' % (moves[0][2], moves[1][2], moves[2][2]))


def make_a_move(symbol):
    x = input('Column (1,2,3):')
    y = input('Row (1,2,3):')
    return {'x': int(x)-1, 'y': int(y)-1, 'symbol': symbol}  #


def register_move(move):
    global moves
    print('Next move:', move)
    moves[move['x']][move['y']] = move['symbol']


def list_results(moves):
    dimension = len(moves)
    columns = []
    diag1 = []
    diag2 = []
    for row in range(0, dimension):
        print('row', row)
        column = []
        for col in range(0, dimension):
            print('col', col)
            column.append(moves[col][row])
        columns.append(column)

        diag1.append(moves[row][row])
        diag2.append(moves[row][dimension-1-row])

    columns.append(diag1)
    columns.append(diag2)

    return columns


def is_ended(moves, game_round):
    check = moves + list_results(moves)
    # todo check if 'o','o','o' or 'x','x','x' is in it
    print ('all moves:', check)
    return game_round > 3
    # print(moves.items())


moves = init_move_history()
players = init_players()
game_round = 0

while not is_ended(moves, game_round):
    clear()
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


