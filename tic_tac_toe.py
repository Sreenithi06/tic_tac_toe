board=[" " for i in range(9)]

def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]}| {board[2]}" )
    print(f"--+--+--+")
    print(f"{board[3]} | {board[4]}| {board[5]}" )
    print(f"--+--+--+")
    print(f"{board[6]} | {board[7]}| {board[8]}" )
    print("\n")
    
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],#rows
        [0,3,6],[1,4,7],[2,5,8],#columns
        [0,4,8],[2,4,6]#diagonals
        ]
        
    for condition in win_conditions:
        if all(board[i]==player for i in condition):
            return True
            
    return False
        
def check_draw():
    return " " not in board
def player_move(player):
    while True:
        try:
             pos = int(input(f"player {player} enter a position from 1 to 9:"))-1
             if pos<0 or pos>8:
                print("invalid position")
                continue
            
             if board[pos] != " ":
                print("spot already taken")
                continue
           
             else:
                 board[pos]=player
                 break
        except ValueError:
            print("invalid value")

def play_game():
    current_player="X"
    print("game started")
    print_board()
    
    while True:
        player_move(current_player)
        print_board()
        
        if check_winner(current_player):
            print(f"{current_player} won ")
            break
        if check_draw():
            print("it is a draw")
            break
        
        current_player="X" if current_player=="O" else "O"
        
play_game()
