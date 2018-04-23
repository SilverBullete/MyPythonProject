import random

print("Welcome to the game Battleship")
print("In the below grid, there is a hidden boat! Find out to sink the battleship")
for i in range(5):
    print("0 0 0 0 0")
name = input("Enter your name: ")
grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
r = random.randint(0, 4)
c = random.randint(0, 4)
times = 0
while True:
    row = eval(input("Guess Row: "))
    col = eval(input("GuessCol:"))
    if row >= 5 or col >= 5:
        print("Oops, that`s not in the ocean.")
        continue
    if row == r and col == c:
        print("Congratulations %s! You sunk my battleship" % name)
        break
    print("You missed my battleship! %s" % name)
    if grid[row][col] == "X":
        print("You guessed that one already.\nEnter new Guess")
    grid[row][col] = "X"
    for k in range(5):
        for j in range(5):
            print(str(grid[k][j]) + " ", end="")
        print()
    print("Enter your guess again")
    if times == 10:
        print("Game Over!")
        break
    times += 1