import os

def print_board(player_pos, enemy_pos):
    """Print the game board with the player's position."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    for i in range(6): # height
        for j in range(10): # width
            if (i, j) == player_pos:
                print('@', end=' ')
            elif (i, j) == enemy_pos:
                print('#', end=' ')
            else:
                print('.', end=' ')
            
        print()

def move_player(player_pos, direction):
    """Move the player based on the input direction."""
    x, y = player_pos

    if direction == 'w' and x > 0:
        x -= 1
    elif direction == 's' and x < 9:
        x += 1
    elif direction == 'a' and y > 0:
        y -= 1
    elif direction == 'd' and y < 9:
        y += 1

    return x, y

def show_enemy(enemy_pos):
    x, y = enemy_pos
    return x, y
    pass

def main():
    player_pos = (0, 0)

    enemy_pos = (2, 2)

    while True:
        print_board(player_pos, enemy_pos)

        # Get user input for movement
        direction = input("Enter a direction (w/a/s/d to move, q to quit): ").lower()

        if player_pos == enemy_pos:
            print("Interact with here!")
            
        if direction == 'q':
            print("Thanks for playing! Exiting...")
            break

        player_pos = move_player(player_pos, direction)
        enemy_pos = show_enemy(enemy_pos)


if __name__ == "__main__":
    main()
