#!/usr/bin/python3

class Xofield:
    xof = [i for i in range(1, 10)]

    def printField(self):
        for i in range(6, -1, -3):
            print ("|", self.xof[i], "|", self.xof[i+1], "|", self.xof[i+2], "|")

    def clearField(self):
        for i in range(0, 9):
            self.xof[i] = ' '

    def putSign(self, player, num):
        if player % 2 == 0:
            self.xof[num - 1] = 'o'
        else:
            self.xof[num - 1] = 'x'

    def checkWin(self):
        return (self.xof[0] == self.xof[1] == self.xof[2] != ' ' or
                self.xof[3] == self.xof[4] == self.xof[5] != ' ' or
                self.xof[6] == self.xof[7] == self.xof[8] != ' ' or
                self.xof[0] == self.xof[3] == self.xof[6] != ' ' or
                self.xof[1] == self.xof[4] == self.xof[7] != ' ' or
                self.xof[2] == self.xof[5] == self.xof[8] != ' ' or
                self.xof[0] == self.xof[4] == self.xof[8] != ' ' or
                self.xof[6] == self.xof[4] == self.xof[2] != ' ')

    def checkFull(self):
        for i in range(0, 9):
            if self.xof[i] == ' ':
                return False
        return True

field = Xofield()
field.printField()
field.clearField()
player = 1
while (1):
    num = input()
    field.putSign(player, int(num))
    field.printField()
    if field.checkWin():
        print ("Congratulations!")
        break
    if field.checkFull():
        print ("Nobody winned :(")
        break
    player += 1
