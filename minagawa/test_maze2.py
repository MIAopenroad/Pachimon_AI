import pygame
from pygame.locals import *
import sys, random
# メッセージダイアログを表示するのに必要な宣言
from tkinter import *
from tkinter import messagebox

# 変数の初期化
maze_w = 31  # 迷路の列数
maze_h = 23  # 迷路の行数
maze = []  # 迷路データ
tile_w = 16
px = 1  # プレイヤーの座標
py = 1

# 色を定義
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
brown = (115, 66, 41)
orange = (233, 168, 38)
maze_color = [white, brown, orange]

Tk().wm_withdraw()


# 迷路を自動的に生成する ---- (*1)
def make_maze():
    global maze, px, py
    px = 1
    py = 1
    tbl = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    # 全部を0(通路)で初期化
    maze = []
    for y in range(0, maze_h):
        row = []
        for x in range(0, maze_w):
            row.append(0)
        maze.append(row)
    # 周囲を1(壁)で初期化
    for x in range(0, maze_w):
        maze[0][x] = 1
        maze[maze_h-1][x] = 1
    for y in range(0, maze_h):
        maze[y][0] = 1
        maze[y][maze_w-1] = 1
    # 棒倒し法で迷路を生成
    for y in range(2, maze_h-2):
        for x in range(2, maze_w-2):
            if x % 2 == 0 and y % 2 == 0:
                r = random.randint(0, 3)
                maze[y][x] = 1
                maze[y+tbl[r][1]][x+tbl[r][0]] = 1
    # ゴールを右下に設定
    maze[maze_h-2][maze_w-2] = 2


# プレイヤーの移動を確認 --- (*2)
def check_key(key):
    global px, py
    old_x, old_y = px, py
    if key == K_LEFT:
        px -= 1
    elif key == K_RIGHT:
        px += 1
    elif key == K_UP:
        py -= 1
    elif key == K_DOWN:
        py += 1
    if maze[py][px] == 2:  # ゴール?
        messagebox.showinfo("ゴール", "宝を見つけた")
        make_maze()
    if maze[py][px] != 0:
        px, py = old_x, old_y


def main():
    # ゲームの初期化処理
    global px, py
    pygame.init()
    pygame.display.set_caption("maze game")
    screen = pygame.display.set_mode((tile_w*maze_w, tile_w*maze_h))
    make_maze()
    # ゲームのメインループ --- (*3)
    while True:
        # 迷路を描画する --- (*4)
        screen.fill(black)
        for y in range(0, maze_h):
            for x in range(0, maze_w):
                v = maze[y][x]
                xx = tile_w * x
                yy = tile_w * y
                pygame.draw.rect(screen,
                                 maze_color[v],
                                 (xx, yy, xx + tile_w, yy+tile_w))
        # プレイヤーを円で描画する
        t2 = tile_w / 2
        pygame.draw.circle(screen, red, (px * tile_w + t2, py * tile_w + t2), t2)
        pygame.display.update()
        # イベントを処理する --- (*5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                check_key(event.key)


if __name__ == '__main__':
    main()