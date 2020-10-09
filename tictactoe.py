import sys

# TicTacToe
# draw the board
# ask for the first player , default will be X
# get input for the current position
# create an available position slots and used position
# check if there is a winner , if not the game continues
# manually check


def choose_player():
    print("""
    RULES:
    use the number pad or number keys to determine the position of your next move
    1 | 2 | 3 
    ----------
    4 | 5 | 6 
    ----------
    7 | 8 | 9 

    then click enter
    """)
    current = int(input('Who wants to go first (1/2):'))
    return current


def draw_board(positions):
    print(f"""\n
        {positions[0]}|{positions[1]}|{positions[2]} 
        ======
        {positions[3]}|{positions[4]}|{positions[5]}        
        ======
        {positions[6]}|{positions[7]}|{positions[8]}
        current:{current_player[1]}
        \n""")


def get_current_symbol(current):
    if current == 1:
        return [1, 'X']
    elif current == 2:
        return [2, 'O']


def pick_spot(current, symbol):
    is_valid = False

    print(f'\nPlayer {current}\'s turn as {symbol}\n')

    while not is_valid:
        selected_position = int(input(
            'Where do you want to put your mark ? Input number for position (0 to exit):'))

        if not selected_position in occupied:
            is_valid = True
        if is_valid:
            break

    board_positions[selected_position - 1] = symbol
    occupied.append(selected_position)

    if(selected_position == 0):
        global is_playing
        is_playing = False


def check_winner(positions, symbol, current):
    # 0 | 1 | 2
    # ----------
    # 3 | 4 | 5
    # ----------
    # 6 | 7 | 8
    global is_playing

    if(positions[0] == positions[1] == positions[2] == symbol or
       positions[3] == positions[4] == positions[5] == symbol or
       positions[6] == positions[7] == positions[8] == symbol or
       positions[0] == positions[3] == positions[6] == symbol or
       positions[1] == positions[4] == positions[7] == symbol or
       positions[2] == positions[5] == positions[8] == symbol or
       positions[2] == positions[4] == positions[6] == symbol or
       positions[0] == positions[4] == positions[8] == symbol
       ):
        print('Player {} is the Winner!'.format(current))
        play_again()
    elif (len(occupied) == 9):
        print("DRAW.")
        play_again()


def play_again():
    global is_playing
    global board_positions
    global occupied
    global current_player
    global is_initialized
    restart = input('Play Again? (y/n)')

    if(restart == 'y'):
        board_positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
        occupied = []
        is_initialized = False

    else:
        is_playing = False


# GAME START
is_playing = True
board_positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
occupied = []
board = """
 1 | 2 | 3 
 ----------
 4 | 5 | 6 
 ----------
 7 | 8 | 9 
"""
current_player = None
is_initialized = False

#  MAIN GAME LOOP
while is_playing:
    # initialize players
    if not is_initialized:
        current_player = choose_player()
        is_initialized = True

    current_player = get_current_symbol(current_player)
    pick_spot(current_player[0], current_player[1])
    draw_board(board_positions)
    check_winner(board_positions, current_player[1], current_player[0])

    if current_player[0] == 1:
        current_player = 2
    else:
        current_player = 1

    if is_playing == False:
        break


print('GAME ENDED')
