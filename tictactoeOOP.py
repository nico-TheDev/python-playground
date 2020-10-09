# TIC TAC TOE OOP

class Tictactoe:
    def __init__(self):
        self.is_playing = True
        self.board_positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
        self.occupied = []
        self.current_player = []
        # initialize the player

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

        if current == 1:
            self.current_player = [1, 'X']
        else:
            self.current_player = [2, 'O']

    def draw_board(self):
        print(f"""\n
        {self.board_positions[0]}|{self.board_positions[1]}|{self.board_positions[2]} 
        ======
        {self.board_positions[3]}|{self.board_positions[4]}|{self.board_positions[5]}        
        ======
        {self.board_positions[6]}|{self.board_positions[7]}|{self.board_positions[8]}
        current:{self.current_player[1]}
        \n""")

    def swap_current_player(self):
        if(self.current_player[0] == 1):
            self.current_player = [2, 'O']
        else:
            self.current_player = [1, 'X']

    def pick_spot(self):
        is_valid = False
        symbol = self.current_player[1]

        print(f'\nPlayer {self.current_player[0]}\'s turn as {symbol}\n')
        # keep asking until the position is valid or not taken
        while not is_valid:
            selected_position = int(input(
                'Where do you want to put your mark ? Input number for position (0 to exit):'))

            if not selected_position in self.occupied:
                is_valid = True
            if is_valid:
                break
        # quit
        if(selected_position == 0):
            self.is_playing = False

        # append the position the the board
        self.board_positions[selected_position - 1] = symbol
        # update the occupied list
        self.occupied.append(selected_position)

    def check_winner(self):
        symbol = self.current_player[1]
        if(self.board_positions[0] == self.board_positions[1] == self.board_positions[2] == symbol or
           self.board_positions[3] == self.board_positions[4] == self.board_positions[5] == symbol or
           self.board_positions[6] == self.board_positions[7] == self.board_positions[8] == symbol or
           self.board_positions[0] == self.board_positions[3] == self.board_positions[6] == symbol or
           self.board_positions[1] == self.board_positions[4] == self.board_positions[7] == symbol or
           self.board_positions[2] == self.board_positions[5] == self.board_positions[8] == symbol or
           self.board_positions[2] == self.board_positions[4] == self.board_positions[6] == symbol or
           self.board_positions[0] == self.board_positions[4] == self.board_positions[8] == symbol
           ):
            print('Player {} is the Winner!'.format(self.current_player[0]))
            self.is_playing = False

        elif len(self.occupied) == 9:
            print("DRAW.")
            self.is_playing = False


# GAME LOOP
game = Tictactoe()

while game.is_playing:
    game.pick_spot()
    game.draw_board()
    game.check_winner()
    game.swap_current_player()
