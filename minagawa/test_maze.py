import sys
import pygame
from pygame.locals import *

# 定数
WIDTH = 320  # 画面横サイズ
HEIGHT = 320  # 画面縦サイズ
B_SIZE = 40   # 辺長
M_SIZE = 20   # 半径
M_DOT = 40   # 移動ドット
W_TIME = 20   # 待ち時間
F_SIZE = 60   # フォントサイズ

# マップ
# (8, 8)
MAP = [[1,0,0,0,0,0,0,0],   # 0
       [1,0,0,1,1,1,1,0],   # 1
       [1,1,1,1,0,0,1,0],   # 2
       [0,0,0,0,1,1,1,0],   # 3
       [0,0,0,0,1,0,0,0],   # 4
       [0,0,0,0,1,1,1,0],   # 5
       [0,0,0,0,0,0,1,1],   # 6
       [0,0,0,0,0,0,0,2]]   # 7


############################
# メイン関数
############################
def main():

    # 迷路描画関数呼び出し
    draw_maze()

    # キー操作関数呼び出し
    input_key()


############################
# 迷路描画関数
############################
def draw_maze():
    # 座標初期化
    x = 0
    y = 0

    # 縦座標
    for b1 in MAP:

        # 横座標
        for b2 in b1:
            if b2 == 0:   # 壁描画
                pygame.draw.rect(surface, (48, 48, 48), (x*B_SIZE, y*B_SIZE, B_SIZE, B_SIZE), 0)
            elif b2 == 1:   # 通路描画
                pygame.draw.rect(surface, (224, 224, 224), (x*B_SIZE, y*B_SIZE, B_SIZE, B_SIZE), 0)
            elif b2 == 2:   # ゴール描画
                pygame.draw.rect(surface, (48, 176, 96), (x*B_SIZE, y*B_SIZE, B_SIZE, B_SIZE), 0)
            x += 1

        # 座標更新
        else:
            x = 0
            y += 1

    # マップ描画
    pygame.display.update()


############################
# キー操作関数
############################
def input_key():

    # 座標初期化
    row = 0         # リスト縦
    col = 0         # リスト横
    now_x = M_SIZE  # 横座標
    now_y = M_SIZE  # 縦座標
    bak_x = M_SIZE  # 横前座標
    bak_y = M_SIZE  # 縦前座標
    e_flag = 0      # 終了フラグ

    # イベント待ち
    while True:

        # ゴール確認
        if MAP[row][col] == 2:

            # 初回のみ
            if e_flag == 0:
                pygame.draw.circle(surface, (255,  0,  0), (now_x,now_y), M_SIZE, 0)
                pygame.draw.circle(surface, (224,224,224), (bak_x,bak_y), M_SIZE, 0)
                pygame.display.update()
                pygame.time.wait(100)
                e_flag = 1

            # テキスト設定
            # text = font.render("GOAL!", True, (224,224,255))

            # ゴール描画
            surface.fill((0, 0, 0))
            surface.blit(drug, (0, 0))

        # 未ゴール
        if e_flag == 0:

            # 移動キャラクター描画
            pygame.draw.circle(surface, (255, 0, 0), (now_x, now_y), M_SIZE, 0)

            # 移動後通路の色に戻す
            if now_x != bak_x or now_y != bak_y:
                pygame.draw.circle(surface, (224, 224, 224), (bak_x, bak_y), M_SIZE, 0)

        # 画面再描画
        pygame.display.update()
        pygame.time.wait(W_TIME)

        # 位置保存
        bak_x = now_x
        bak_y = now_y

        # イベント取得
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_LEFT:
                    if (now_x > 0 + B_SIZE) and (MAP[row][col-1] != 0):
                        col -= 1
                        now_x -= M_DOT
                if event.key == K_RIGHT:
                    if (now_x < WIDTH - B_SIZE) and (MAP[row][col+1] != 0):
                        col += 1
                        now_x += M_DOT
                if event.key == K_UP:
                    if (now_y > 0 + B_SIZE) and (MAP[row-1][col] != 0):
                        row -= 1
                        now_y -= M_DOT
                if event.key == K_DOWN:
                    if (now_y < HEIGHT - B_SIZE) and (MAP[row+1][col] != 0):
                        row += 1
                        now_y += M_DOT


############################
# 終了関数
############################
def exit():
    pygame.quit()
    sys.exit()


############################
# メイン関数呼び出し
if __name__ == "__main__":

    # 画面初期化
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    # font = pygame.font.Font(None, F_SIZE)
    drug = pygame.image.load("/Users/minagawa/PycharmProjects/pythonProject2/image/monster/dragMarile.jpeg")
    drug = pygame.transform.scale(drug, (WIDTH, HEIGHT))

    # 処理開始
    main()