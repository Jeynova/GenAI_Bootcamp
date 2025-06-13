import random


class Board:
    def __init__(self,width,height):
        self.width,self.height=width,height
        self.grid=[[False]*width for _ in range(height)]
    def set_live(self,coords):
        for x,y in coords:
            if 0<=x<self.width and 0<=y<self.height:
                self.grid[y][x]=True

    def count_neighbors(self,x,y):
        total=0
        for posY in (-1,0,1):
            for posX in (-1,0,1):
                if posX==posY==0:continue
                newX,newY=x+posX,y+posY
                if 0<=newX<self.width and 0<=newY<self.height and self.grid[newY][newX]:
                    total+=1
        return total

    def step(self):
            self._add_frame()                                #1. élargit
            new=[[False]*self.width for _ in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    live=self.count_neighbors(x,y)
                    new[y][x]=live==3 or (self.grid[y][x] and live in (2,3))
            self.grid=new
            self._trim_frame()    
        
    def _add_frame(self):
            #ajoute une ceinture de cellules mortes tout autour
            self.grid.insert(0, [False]*self.width)          #ligne vide en haut
            self.grid.append([False]*self.width)             #ligne vide en bas
            self.height += 2
            for row in self.grid:
                row.insert(0, False)                         #colonne vide gauche
                row.append(False)                            #colonne vide droite
            self.width += 2

    def _trim_frame(self):
        #supprime les bords complets de cellules mortes (évite d’infler)
        #haut
        while self.height>1 and all(not c for c in self.grid[0]):
            self.grid.pop(0); self.height-=1
        #bas
        while self.height>1 and all(not c for c in self.grid[-1]):
            self.grid.pop(); self.height-=1
        #gauche
        while self.width>1 and all(not row[0] for row in self.grid):
            for row in self.grid: row.pop(0)
            self.width-=1
        #droite
        while self.width>1 and all(not row[-1] for row in self.grid):
            for row in self.grid: row.pop()
            self.width-=1

class Game:
    def __init__(self,board,delay=0.2):
        self.board=board
        self.delay=delay

    def display(self):
        import os,time
        os.system("cls" if os.name=="nt" else "clear")
        for row in self.board.grid:
            print("".join("█" if cell else " " for cell in row))
        time.sleep(self.delay)

    def run(self,steps=100):
        for _ in range(steps):
            self.display()
            self.board.step()

if __name__=="__main__":
    gun=[
 (1,5),(2,5),(1,6),(2,6),
 (13,5),(14,5),(12,6),(16,6),(11,7),(17,7),(11,8),(17,8),
 (14,9),(12,10),(16,10),(13,11),(14,11),
 (25,3),(23,4),(25,4),(21,5),(22,5),(21,6),(22,6),(21,7),(22,7),
 (23,8),(25,8),(25,9),
 (35,5),(36,5),(35,6),(36,6)
]
b=Board(60,40)
b.set_live(gun)
Game(b).run(500)