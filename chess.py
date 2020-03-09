# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:03:43 2020

@author: Elisha and Abigail
"""
class king:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def r(self):
        self.x = self.x + 1
    def l(self):
        self.x = self.x - 1
    def d(self):
        self.y = self.y - 1
    def u(self):
        self.y = self.y + 1    
        
    def returnPos(self):
        print(self.x, self.y)
        
    def TR(self):
        self.r()
        self.u()
    def R(self):
        self.r()
    def BR(self):
        self.r()
        self.d()
    def B(self):
        self.d()
    def BL(self):
        self.l()
        self.d()
    def L(self):
        self.l()
    def TL(self):
        self.l()
        self.u()
    def T(self):
        self.u()
            
class queen:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def r(self):
        self.num = input()
        self.x = self.x + (int(self.num) * 1)
    def l(self):
        self.num = input()
        self.x = self.x - (int(self.num) * 1)
    def d(self):
        self.num = input()
        self.y = self.y - (int(self.num) * 1)
    def u(self):
        self.num = input()
        self.y = self.y + (int(self.num) * 1)
        
    def returnPos(self):
        print(self.x, self.y)
        
    def TR(self):
        self.r()
        self.u()
    def R(self):
        self.r()
    def BR(self):
        self.r()
        self.d()
    def B(self):
        self.d()
    def BL(self):
        self.l()
        self.d()
    def L(self):
        self.l()
    def TL(self):
        self.l()
        self.u()
    def T(self):
        self.u()
    
        
class bishop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def r(self):
        self.num = input()
        self.x = self.x + (int(self.num) * 1)
    def l(self):
        self.num = input()
        self.x = self.x - (int(self.num) * 1)
    def d(self):
        self.num = input()
        self.y = self.y - (int(self.num) * 1)
    def u(self):
        self.num = input()
        self.y = self.y + (int(self.num) * 1)
        
    def returnPos(self):
        print(self.x, self.y)
        
    def TR(self):
        self.r()
        self.u()
        
    def BR(self):
        self.r()
        self.d()
        
    def BL(self):
        self.l()
        self.d()
    
    def TL(self):
        self.l()
        self.u()
    

class horse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def u(self):
        self.y = self.y + 2
    def r(self):
        self.x = self.x + 2
    def d(self):
        self.y = self.y - 2
    def l(self):
        self.x = self.x - 2
    def U(self):
        self.y = self.y + 1
    def R(self):
        self.x = self.x + 1
    def D(self):
        self.y = self.y - 1
    def L(self):
        self.x = self.x - 1
        
    def returnPos(self):
        print(self.x, self.y)
        
    def tL(self):
        self.u()
        self.L()
    def tR(self):
        self.u()
        self.R()
    def rT(self):
        self.r()
        self.U()
    def rD(self):
        self.r()
        self.D()
    def dR(self):
        self.d()
        self.R()
    def dL(self):
        self.d()
        self.L()
    def lD(self):
        self.l()
        self.D()
    def lT(self):
        self.l()
        self.U()
        
class rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def r(self):
        self.num = input()
        self.x = self.x + (int(self.num) * 1)
    def l(self):
        self.num = input()
        self.x = self.x - (int(self.num) * 1)
    def d(self):
        self.num = input()
        self.y = self.y - (int(self.num) * 1)
    def u(self):
        self.num = input()
        self.y = self.y + (int(self.num) * 1)
        
    def returnPos(self):
        print(self.x, self.y)

class pawn:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        
    def wu(self):
        self.y = self.y + 1        
    def wrcut(self):
        self.u()
        self.x = self.x + 1        
    def wlcut(self):
        self.u()
        self.x = self.x - 1
        
    def returnPos(self):
        print(self.x, self.y)
        
    def bu(self):
        self.y = self.y - 1        
    def brcut(self):
        self.u()
        self.x = self.x + 1        
    def blcut(self):
        self.u()
        self.x = self.x - 1
        
grid_size = []
x = 1

while x <= 64:
    grid_size.append(x)
    x =+ 1
    if x == 64:
        break
        
#White Pieces:
#wKing = king(5,1)
#wQueen = queen(4,1)
#wBishop1 = bishop(3,1)
#wBishop2 = bishop(6,1)
#wHorse1 = horse(2,1)
#wHorse2 = horse(7,1)
#wRook1 = rook(1,1)
#wRook2 = rook(8,1)
#wpawn1 = pawn(1,2)
#wpawn2 = pawn(2,2)
#wpawn3 = pawn(3,2)
#wpawn4 = pawn(4,2)
#wpawn5 = pawn(5,2)
#wpawn6 = pawn(6,2)
#wpawn7 = pawn(7,2)
#wpawn8 = pawn(8,2)
##Black Pieces:
#bKing = king(5,8)
#bQueen = queen(4,8)
#bBishop1 = bishop(3,8)
#bBishop2 = bishop(6,8)
#bHorse1 = horse(2,8)
#bHorse2 = horse(7,8)
#bPawn1 = pawn(1,8)
#bPawn2 = pawn(8,8)
#bPawn1 = pawn(1,7)
#bPawn2 = pawn(2,7)
#bPawn3 = pawn(3,7)
#bPawn4 = pawn(4,7)
#bPawn5 = pawn(5,7)
#bPawn6 = pawn(6,7)
#bPawn7 = pawn(7,7)
#bPawn8 = pawn(8,7)
#    