import time, os, random

def display1(chars):
    os.system('cls')
    for row in chars:
        print(''.join(row))

def display2(chars):
    os.system('cls')
    print('\n'.join(''.join(row) for row in chars))


chars = []
for i in range(40):
    chars.append(["-"]*40)

for i in range(100):
    r = random.randint(0,39)
    c = random.randint(0,39)
    chars[r][c] = "X"
    time.sleep(0.1)
    display1(chars)

os.system('cls')
time.sleep(1)

chars = []
for i in range(40):
    chars.append(["-"]*40)

for i in range(100):
    r = random.randint(0,39)
    c = random.randint(0,39)
    chars[r][c] = "X"
    time.sleep(0.1)
    display2(chars)