#!/usr/bin/env python
# coding: utf-8

# In[57]:


# ------- Global Variables --------


# In[58]:


# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# In[59]:


# If game is still going
game_still_going = True


# In[60]:


# Who won? Or tie?
winner = None


# In[61]:


# Whos turn is it?
current_player = "X"

# --------- Functions -----------


# In[62]:


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# In[63]:


# Play a game of tic tac toe
def play_game():
    
    display_board()
    
    # While the game is still going
    while game_still_going:
        
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        # Check if the game has ended
        check_if_game_over()
        
        # Flip to the other player
        flip_player()
        
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# In[64]:


def handle_turn(player):
    
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:
    
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
    
        position = int(position) - 1
    
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    
    board[position] = player
    
    display_board()


# In[65]:


def check_if_game_over():
    check_for_winner()
    check_if_tie()


# In[66]:


def check_for_winner():
    
    # Set up global variables
    global winner
    
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # ther was no win
        winner = None
    return


# In[67]:


def check_rows():
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# In[68]:


def check_columns():
    # Set up global variables
    global game_still_going
    # check if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# In[69]:


def check_diagonals():
    # Set up global variables
    global game_still_going
    # check if any of the diagonals have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


# In[70]:


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# In[71]:


def flip_player():
    # global variables we need
    global current_player
    # if the current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    # if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


# In[72]:


play_game()


# In[ ]:




