## -*- coding: utf-8 -*-
#"""
#Created on Tue Mar  3 12:03:43 2020
#
#@author: Elisha and Abigail
#"""

import tkinter
from tkinter import *
import re


b = tkinter.Tk()


placement = {}
position = []

class king:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
    def r(self):
        self.x = self.x + 1
    def l(self):
        self.x = self.x - 1
    def d(self):
        self.y = self.y - 1
    def u(self):
        self.y = self.y + 1    
        
    def returnPos(self):
        pos = self.x, self.y
        print(pos)
        
    def TR(self):
        self.r()
        self.u()
        check_placement()
    def R(self):
        self.r()
        check_placement()
    def BR(self):
        self.r()
        self.d()
        check_placement()
    def B(self):
        self.d()
        check_placement()
    def BL(self):
        self.l()
        self.d()
        check_placement()
    def L(self):
        self.l()
        check_placement()
    def TL(self):
        self.l()
        self.u()
        check_placement()
    def T(self):
        self.u()
        check_placement()
            
class queen:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
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
        pos = self.x, self.y
        print(pos)
        
    def TR(self):
        self.r()
        self.u()
        check_placement()
    def R(self):
        self.r()
        check_placement()
    def BR(self):
        self.r()
        self.d()
        check_placement()
    def B(self):
        self.d()
        check_placement()
    def BL(self):
        self.l()
        self.d()
        check_placement()
    def L(self):
        self.l()
        check_placement()
    def TL(self):
        self.l()
        self.u()
        check_placement()
    def T(self):
        self.u()
        check_placement()
    
        
class bishop:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
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
        pos = self.x, self.y
        print(pos)
        
    def TR(self):
        self.r()
        self.u()
        check_placement()
        
    def BR(self):
        self.r()
        self.d()
        check_placement()
        
    def BL(self):
        self.l()
        self.d()
        check_placement()
        
    def TL(self):
        self.l()
        self.u()
        check_placement()
    

class horse:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
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
        pos = self.x, self.y
        print(pos)
        
    def tL(self):
        self.u()
        self.L()
        check_placement()
    def tR(self):
        self.u()
        self.R()
        check_placement()
    def rT(self):
        self.r()
        self.U()
        check_placement()
    def rD(self):
        self.r()
        self.D()
        check_placement()
    def dR(self):
        self.d()
        self.R()
        check_placement()
    def dL(self):
        self.d()
        self.L()
        check_placement()
    def lD(self):
        self.l()
        self.D()
        check_placement()
    def lT(self):
        self.l()
        self.U()
        check_placement()
        
class rook:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
    def r(self):
        self.num = input()
        self.x = self.x + (int(self.num) * 1)
        check_placement()
    def l(self):
        self.num = input()
        self.x = self.x - (int(self.num) * 1)
        check_placement()
    def d(self):
        self.num = input()
        self.y = self.y - (int(self.num) * 1)
        check_placement()
    def u(self):
        self.num = input()
        self.y = self.y + (int(self.num) * 1)
        check_placement()
        
    def returnPos(self):
        pos = self.x, self.y
        print(pos)

class pawn:
    def __init__(self, name, x, y):
        self.x = x
        self.name = name
        self.y = y
        
        pos = (10 * self.x) + self.y
        position.append(pos)
        
        placement[self.name] = pos
        
    def wu(self):
        self.y = self.y + 1  
    def r(self):
        self.x = self.x + 1
    def l(self):
        self.x = self.x - 1
    
    def wrcut(self):
        self.u()
        self.r() 
        check_placement()
    def wlcut(self):
        self.u()
        self.l()
        check_placement()
        
    def returnPos(self):
        pos = self.x, self.y
        print(pos)
        
    def bu(self):
        self.y = self.y - 1 
        
    def brcut(self):
        self.u()
        self.l()  
        check_placement()
    def blcut(self):
        self.u()
        self.r()
        check_placement()
        

#White Pieces:
wKing = king("White_King",5,1)
wQueen = queen("White_Queen",4,1)
wBishop1 = bishop("White_Bishop1",3,1)
wBishop2 = bishop("White_Bishop2",6,1)
wHorse1 = horse("White_Horse1",2,1)
wHorse2 = horse("White_Horse2",7,1)
wRook1 = rook("White_Rook1",1,1)
wRook2 = rook("White_Rook2",8,1)
wPawn1 = pawn("White_Pawn1",1,2)
wPawn2 = pawn("White_Pawn2",2,2)
wPawn3 = pawn("White_Pawn3",3,2)
wPawn4 = pawn("White_Pawn4",4,2)
wPawn5 = pawn("White_Pawn5",5,2)
wPawn6 = pawn("White_Pawn6",6,2)
wPawn7 = pawn("White_Pawn7",7,2)
wPawn8 = pawn("White_Pawn8",8,2)

#Black Pieces:
bKing = king("Black_King",5,8)
bQueen = queen("Black_Queen",4,8)
bBishop1 = bishop("Black_Bishop1",3,8)
bBishop2 = bishop("Black_Bishop2",6,8)
bHorse1 = horse("Black_Horse1",2,8)
bHorse2 = horse("Black_Horse2",7,8)
bPawn1 = pawn("Black_Rook1",1,8)
bPawn2 = pawn("Black_Rook2",8,8)
bPawn1 = pawn("Black_Pawn1",1,7)
bPawn2 = pawn("Black_Pawn2",2,7)
bPawn3 = pawn("Black_Pawn3",3,7)
bPawn4 = pawn("Black_Pawn4",4,7)
bPawn5 = pawn("Black_Pawn5",5,7)
bPawn6 = pawn("Black_Pawn6",6,7)
bPawn7 = pawn("Black_Pawn7",7,7)
bPawn8 = pawn("Black_Pawn8",8,7)


def check_placement():
    for x in position:
        y = re.findall("[0-9]", x)
        if not (y):
            defaultpos = x
            print(defaultpos)
        elif (y):
            x = defaultpos
            print(x)
    
check_placement()
        