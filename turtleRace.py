import random
import turtle
from time import sleep


class Player:
    __numbers = 0  # 记录玩家个数
    __distance = 200  # 运动距离
    __startPosition = 200  # 起始纵坐标

    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        # 每个玩家的起始纵坐标相差50
        Player.__startPosition -= 50
        # 每创建一个新玩家，numbers + 1
        Player.__numbers += 1

    def getNumbers(self):
        return Player.numbers

    def getStarPosition(self):
        return Player.__startPosition

    def getDistance(self):
        return Player.distance

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color


class Game:
    turtleList = []  # 存放创建的turtle对象

    def __init__(self):
        self.__player = []  # 存放玩家对象
        self.__result = []  # 将turtleList的索引按完成先后排序

    def setResult(self, index):
        # 将刚完成的turtleList中turtle的索引加入结果
        if index not in self.__result:
            self.__result.append(index)

    def getResult(self):
        return self.__result

    def getPlayer(self):
        return self.__player

    def drawLines(self):
        line1 = turtle.Turtle()
        # 画笔路径不可见
        line1._tracer(False)
        # 画笔不可见
        line1.hideturtle()
        # 抬笔
        line1.penup()
        # 移动画笔
        line1.setpos(-250, 200)
        # 居中写Start
        line1.write("Start", False, "center", 10)
        # 落笔
        line1.pendown()
        # 移动画线
        line1.goto(-250, -200)
        line2 = turtle.Turtle()
        line2._tracer(False)
        line2.hideturtle()
        line2.penup()
        line2.setpos(250, 200)
        line2.write("End", False, "center", 10)
        line2.pendown()
        line2.goto(250, -200)
        # 路径可见
        line1._tracer(True)
        line2._tracer(True)

    def addPlayer(self):
        screen = turtle.Screen()
        # 输入name和color
        name = screen.textinput('Enter your name', "Enter your name: ")
        color = screen.textinput("Enter your favorite color", "Enter your favorite color: ")
        # 创建Player对象
        player = Player(name, color)
        # 将创建的Player对象加入list
        self.__player.append(player)
        # 画出Player所对应的turtle
        tur = turtle.Pen()
        tur.shape("turtle")
        tur.color(player.getColor())
        tur._tracer(False)
        tur.penup()
        # 将turtle移动到起点
        tur.setpos(-265, player.getStarPosition())
        tur.pendown()
        tur._tracer(True)
        # 将player的name写在起点
        tur.write(player.getName(), True, "right", 10)
        Game.turtleList.append(tur)

    def ifGameEnd(self):
        # 若全部turtle到达终点则游戏结束
        for i in range(len(Game.turtleList)):
            if Game.turtleList[i].xcor() < 235:
                return False
        return True

    def race(self):
        while True:
            # 随机挑选Player进行移动
            j = random.randint(0, len(Game.turtleList) - 1)
            # 随机生成速度
            Game.turtleList[j].speed(random.randint(1, 3))
            if Game.turtleList[j].xcor() >= 235:
                Game.setResult(self, j)
                continue
            # 移动
            Game.turtleList[j].forward(4)
            if Game.ifGameEnd(self):
                Game.setResult(self, j)
                break

    def showResult(self):
        re = turtle.Pen()
        re.penup()
        re.hideturtle()
        y = 200 - 100 * len(self.getPlayer())
        re.setpos(-200, y)
        # 构造result字符串
        s = "                       Result"
        for i, j in enumerate(range(len(Game.turtleList))):
            s += "\n\n              %d                  %s " % (
                i + 1, Game.getPlayer(self)[Game.getResult(self)[i]].getName())
        # 输出结果
        re.write(s, True, "left", 10)


screen = turtle.Screen()
screen.title("Turtle Race")
game = Game()
game.drawLines()
while True:
    game.addPlayer()
    boolean = screen.textinput("Continue to add player?", "Continue to add player? Y for yes, other for no")
    if (boolean != "Y"):
        break
game.race()
game.showResult()
sleep(10)
