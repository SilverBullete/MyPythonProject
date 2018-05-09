import random

#欢迎界面
print("Welcome to the game Battleship")
print("In the below grid, there is a hidden boat! Find out to sink the battleship")
#打印初始的5*5表格
for i in range(5):
    print("0 0 0 0 0")
name = input("Enter your name: ")
#初始化表格的二维数组
grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#随机生成战舰位置
r = random.randint(0, 4)
c = random.randint(0, 4)
#记录猜测次数
times = 0
while True:
    #输入猜测的坐标
    row = eval(input("Guess Row: "))
    col = eval(input("GuessCol:"))
    #限制输入的坐标
    if row >= 5 or col >= 5:
        print("Oops, that`s not in the ocean.")
        continue
    #找到战舰坐标 游戏结束
    if row == r and col == c:
        print("Congratulations %s! You sunk my battleship" % name)
        break
    print("You missed my battleship! %s" % name)
    #判断是否此坐标已被选过
    if grid[row][col] == "X":
        print("You guessed that one already.\nEnter new Guess")
    #将错误的坐标位置用X替换
    grid[row][col] = "X"
    #打印表格
    for k in range(5):
        for j in range(5):
            print(str(grid[k][j]) + " ", end="")
        print()
    print("Enter your guess again")
    #猜测次数达到十次游戏结束
    if times == 10:
        print("Game Over!")
        break
    times += 1
