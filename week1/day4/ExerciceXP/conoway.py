import os
import time
from typing import List, Tuple

class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def set_live(self, coords: List[Tuple[int, int]]):
        for x, y in coords:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = True

    def count_neighbors(self, x: int, y: int) -> int:
        total = 0
        for offset_y in (-1, 0, 1):
            for offset_x in (-1, 0, 1):
                if offset_x == 0 and offset_y == 0:
                    continue
                neighbor_x = x + offset_x
                neighbor_y = y + offset_y
                if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                    if self.grid[neighbor_y][neighbor_x]:
                        total += 1
        return total

    def step(self):
        self._add_frame()
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if neighbors == 3 or (self.grid[y][x] and neighbors in (2, 3)):
                    new_grid[y][x] = True
        self.grid = new_grid
        self._trim_frame()

    def _add_frame(self):
        self.grid.insert(0, [False] * self.width)
        self.grid.append([False] * self.width)
        self.height += 2
        for row in self.grid:
            row.insert(0, False)
            row.append(False)
        self.width += 2

    def _trim_frame(self):
        while self.height > 1 and all(not c for c in self.grid[0]):
            self.grid.pop(0)
            self.height -= 1
        while self.height > 1 and all(not c for c in self.grid[-1]):
            self.grid.pop()
            self.height -= 1
        while self.width > 1 and all(not row[0] for row in self.grid):
            for row in self.grid:
                row.pop(0)
            self.width -= 1
        while self.width > 1 and all(not row[-1] for row in self.grid):
            for row in self.grid:
                row.pop()
            self.width -= 1


class Game:
    def __init__(self, board: Board, delay: float = 0.2):
        self.board = board
        self.delay = delay

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("╔" + "══" * self.board.width + "╗")
        for row in self.board.grid:
            line = "║" + "".join("■ " if cell else "□ " for cell in row) + "║"
            print(line)
        print("╚" + "══" * self.board.width + "╝")
        time.sleep(self.delay)

    def run(self, steps: int = 100):
        for _ in range(steps):
            self.display()
            self.board.step()


if __name__ == "__main__":
    gun = [
        (1, 5), (2, 5), (1, 6), (2, 6),
        (13, 5), (14, 5), (12, 6), (16, 6), (11, 7), (17, 7),
        (11, 8), (17, 8), (14, 9), (12, 10), (16, 10), (13, 11), (14, 11),
        (25, 3), (23, 4), (25, 4), (21, 5), (22, 5), (21, 6),
        (22, 6), (21, 7), (22, 7), (23, 8), (25, 8), (25, 9),
        (35, 5), (36, 5), (35, 6), (36, 6)
    ]

    board = Board(60, 40)
    board.set_live(gun)
    Game(board).run(500)
