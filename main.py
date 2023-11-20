import os, time

# conditional vars
gameloop = True
gameFPS = 24
gamestart = time.time()
x, y = 7, 10

# function for screen clear
def srcclr(): os.system("cls")

# function draw()
def drawSpace(): print("+---------------------------------------------+\n" + 
                       "|-------- WELCOME TO THE GAME WORLD ----------|\n" + 
                       "+---------------------------------------------+") 

#  main game-loop
while gameloop:
    srcclr()

    # demo.main()
    # drawSpace()
    print("hello world: A simple FPS demo!")
    print(time.time() - gamestart)

    # frame buffer
    time.sleep(1/gameFPS)