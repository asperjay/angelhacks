import random
# one square
class Square:
    def __init__(self,pos,color='black'):
        self.pos=pos
        self.color=color
    def changeColor(self,new):
        self.color=new
# collection of squares
class Block:
    def __init__(self,rotation,centerPos, shape):
        self.rotation=rotation
        (centerX,centerY)=centerPos
        if shape=='.':
            self.squares=[centerPos] #use shape to set squares
        self.shape=shape
    def createRandomShape():
        return random.choice('.')
# 10x20 grid of blocks and black squares
class Grid:
    def __init__(self):
       self.grid=[]
       for row in range(19):
           currentRow=[]
           for col in range(9):
               currentRow.append(Square((row,col))
            grid.append(currentRow)
    
# grid and hold and next
class Board:
    def __init__(self):
        self.grid=Grid()
        self.hold=None
        self.next=[]
        for i in range(5):
            self.next.append(createRandomShape())
