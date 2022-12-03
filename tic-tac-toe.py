ALL_SPACES = [1,2,3,4,5,6,7,8,9]
X = "X"
O = "O"
BLANK = " "

def main():
    leading_player, next_player = X, O # X goes first, O goes second
    
    current_board = create_board()
    print("Welcome to Tic-Tac-Toe game.")

    while True:
        display_board(current_board)
        
        move = None
        while True: # Get a valid move until it's given.
            print(f"It's {leading_player}'s turn. What is your move?(1-9)")
            move = input("> ")
            if not move.isdecimal() or not (1 <= int(move) <= 9):
                print("You didin't type in a valid move, please type a value between 1-9")
            elif current_board[int(move)] != BLANK:
                display_board(current_board)
                print("It is already taken, please give a value that's not taken.")
            else:
                break
        update_board(current_board, move,leading_player)
        
        if is_winner(current_board, leading_player):
            display_board(current_board)
            print(leading_player + " Has won!")
            print("Thanks for playing!")
            break

        if is_it_tie(current_board):
            display_board(current_board)
            print("This game is a tie!")
            print("Thanks for playing!")
            break

        leading_player, next_player = next_player, leading_player
      
def create_board():
    d = {}
    for i in ALL_SPACES:
        d[i] = BLANK
    return d


def display_board(board):
    print("""
    {}|{}|{}    1  2  3
    -+-+- 
    {}|{}|{}    4  5  6
    -+-+- 
    {}|{}|{}    7  8  9
    """.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))


def update_board(current_board, move, leading_player):

    current_board[int(move)] = leading_player
    

def is_winner(current_board, leading_player):
    return (current_board[1] == current_board[2]==current_board[3]==leading_player or
            current_board[4] == current_board[5]==current_board[6]==leading_player or
            current_board[7] == current_board[8]==current_board[9]==leading_player or
            current_board[1] == current_board[4]==current_board[7]==leading_player or
            current_board[2] == current_board[5]==current_board[8]==leading_player or
            current_board[3] == current_board[6]==current_board[9]==leading_player or
            current_board[1] == current_board[5]==current_board[9]==leading_player or
            current_board[3] == current_board[5]==current_board[7]==leading_player )

def is_it_tie(current_board):
    
    for v in current_board.values():
        if v == BLANK:
            return False
    return True

main()






