# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((400, 400))    # 大きさ400*300の画面を生成
    pygame.display.set_caption("Gangi")              # タイトルバーに表示する文字
    logo = pygame.image.load("./image/background/summer_beach.jpeg").convert_alpha()
    screen_width, screen_height = screen.get_width(), screen.get_height()
    resized_back = pygame.transform.scale(logo, (screen_width, screen_height))

    monster = pygame.image.load("./image/monster/dragMarile.jpeg")
    resized_monster = pygame.transform.scale(monster, (screen_width//10, screen_height//10))
    monster_rect = resized_monster.get_rect()
    monster_width, monster_height = monster_rect.width, monster_rect.height
    monster_rect.center = (screen_width // 2, screen_height // 2)

    speed = 1
    clock = pygame.time.Clock()

    while (1):
        # イベント処理
        # keyおした回数for分回る
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if monster_rect.x - speed < 0:
                continue
            else:
                monster_rect.x -= speed
        elif keys[pygame.K_RIGHT]:
            if monster_rect.x + monster_width + speed > screen_width:
                continue
            else:
                monster_rect.x += speed
        elif keys[pygame.K_UP]:
            if monster_rect.y - speed < 0:
                continue
            else:
                monster_rect.y -= speed
        elif keys[pygame.K_DOWN]:
            if monster_rect.y + monster_height + speed > screen_height:
                continue
            else:
                monster_rect.y += speed

        screen.fill((0, 0, 0))        # 画面を黒色(#000000)に塗りつぶし
        screen.blit(resized_back, (0, 0))
        screen.blit(resized_monster, monster_rect)
        pygame.display.update()     # 画面を更新

        clock.tick(60)


if __name__ == "__main__":
    main()
