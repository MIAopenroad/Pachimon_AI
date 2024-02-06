# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pygame import transform, Rect
import sys


def swamp_check(x, y):
    if 100 < x < 200 and 100 < y < 200:
        return True
    else:
        return False


def main():
    pygame.init()                                   # Pygameの初期化
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height))    # 大きさ400*300の画面を生成
    pygame.display.set_caption("Pokemon")              # タイトルバーに表示する文字

    # playerとmapの画像読み込み
    map_image = pygame.image.load("/Users/minagawa/PycharmProjects/pythonProject2/image/background/fake_map.jpeg").convert_alpha()
    monster = pygame.image.load("/Users/minagawa/PycharmProjects/pythonProject2/image/monster/catagirus.png")

    # playerとmapの初期設定
    map_image = transform.scale(map_image, (width, height))

    monster = transform.scale(monster, (width//5, height//5))  # monsterの画像を背景の10分の1に
    monster_rect = monster.get_rect()  # monsterの長方形を取得
    monster_width, monster_height = monster_rect.width, monster_rect.height  # 長方形の横幅と縦幅を取得しておく
    monster_rect.center = (width // 2, height // 2)  # 中心をディスプレイのセンターに

    # playerのspeed設定
    speed = 2
    clock = pygame.time.Clock()

    # カメラの位置を初期化
    camera_width, camera_height = width // 5, height // 5

    while True:
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

        # key入力の制御
        keys = pygame.key.get_pressed()
        if swamp_check(monster_rect.x, monster_rect.y):
            speed = 1
        else:
            speed = 2

        if keys[pygame.K_LEFT]:
            if monster_rect.x - speed < 0:
                continue
            else:
                monster_rect.x -= speed
        elif keys[pygame.K_RIGHT]:
            if monster_rect.x + monster_width + speed > width:
                continue
            else:
                monster_rect.x += speed
        elif keys[pygame.K_UP]:
            if monster_rect.y - speed < 0:
                continue
            else:
                monster_rect.y -= speed
        elif keys[pygame.K_DOWN]:
            if monster_rect.y + monster_height + speed > height:
                continue
            else:
                monster_rect.y += speed

        # プレイヤーの座標にカメラを連動させる
        camera_x = max(0, monster_rect.x)
        camera_y = max(0, monster_rect.y)

        # subsurfaceがマップの範囲外を参照しないようにする
        subsurface_rect = pygame.Rect(camera_x, camera_y, camera_width, camera_height)
        subsurface_rect.clamp_ip(pygame.Rect(0, 0, width, height))

        screen.fill((0, 0, 0))        # 画面を黒色(#000000)に塗りつぶし
        screen.blit(map_image, map_image.get_rect())
        screen.blit(transform.scale(map_image.subsurface(subsurface_rect),
                                    (width, height)), (0, 0))
        screen.blit(monster, (monster_rect.x, monster_rect.y))
        pygame.display.update()     # 画面を更新

        clock.tick(30)


if __name__ == "__main__":
    main()
