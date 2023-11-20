import os, time, keyboard

# conditional vars
gameloop, play = True, True
gameTime = time.time()
player = "@"
empty = "."
x, y = 0, 0

# function for screen clear
def cls(): os.system('cls');

gameMap = [[".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."],
           [".", ".", ".", ".", ".",".", ".", ".",".", "."]]


y_pos = len(gameMap)-1
x_pos = len(gameMap[0])-1

# current = gameMap[y_pos][x_pos]

def test(array):
    cls()
    for item in array:
        print(' '.join(item))
    time.sleep(0.09)

def changePOS(y, x):
    gameMap[y][x] = player
    print(y, x)


#  main game-loop
while gameloop:
    
    #  player controller
    if keyboard.is_pressed('right arrow'):
            # print("U have pressed 'D' key")
        if x < x_pos:
            x += 1
            gameMap[y][x-1] = empty

    elif keyboard.is_pressed('left arrow'):
        if x > 0:
            x -= 1
            gameMap[y][x+1] = empty

    elif keyboard.is_pressed('up arrow'):
        if y > 0:
            y -= 1
            gameMap[y+1][x] = empty
        
    elif keyboard.is_pressed('down arrow'):
        if y < y_pos:
            y += 1
            gameMap[y-1][x] = empty   
    
    #  end of player ctrl

    if play: 
        # print("hello world: A simple FPS demo! \n")
        test(gameMap) # array-print
        changePOS(y, x)
