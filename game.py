import pygame
import random

# Playerクラス
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed
        self.shoot_delay = 300  # ビームの発射間隔（ミリ秒）
        self.last_shot_time = pygame.time.get_ticks()  # 最後にビームを発射した時刻

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            # 画面外に出ないように制限
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            # 画面外に出ないように制限
            if self.rect.right > window_width:
                self.rect.right = window_width

        if keys[pygame.K_SPACE]:
            self.shoot_beam()

        if keys[pygame.K_RSHIFT]:
            self.shoot_beam(triple=True)  # 右シフトキーが押されたら3倍のビームを発射

        if keys[pygame.K_q]:
            self.shoot_beam(super_beam=True)  # Qキーが押されたら特大ビームを発射


    def shoot_beam(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_delay:
            beam = Beam(beam_image, self.rect.centerx, self.rect.top, 10)
            all_sprites.add(beam)
            beams.add(beam)
            self.last_shot_time = current_time

    def shoot_beam(self, triple=False, upward=False, super_beam=False):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_delay:
            if triple:
                # ビームを3倍に増やす
                beam_x_offsets = [-17, 0, 17]  # ビームの横方向オフセット
                for offset in beam_x_offsets:
                    beam = Beam(beam_image, self.rect.centerx + offset, self.rect.top, 10)
                    all_sprites.add(beam)
                    beams.add(beam)
            elif super_beam:
                # 特大ビームを発射
                super_beam = Beam(beam_image, self.rect.centerx-35, self.rect.top, 10)
                super_beam.image = pygame.transform.scale(super_beam.image, (super_beam.rect.width * 4, super_beam.rect.height * 4))
                all_sprites.add(super_beam)
                beams.add(super_beam)
            else:
                # 通常のビームを発射
                beam = Beam(beam_image, self.rect.centerx, self.rect.top, 10)
                all_sprites.add(beam)
                beams.add(beam)

            self.last_shot_time = current_time

# ビームクラス
class Beam(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

        # 画面外に出たらビームを削除
        if self.rect.bottom < 0:
            self.kill()

# ゲームの初期化
pygame.init()

# ゲームウィンドウの設定
window_width = 600
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("画像を左右に動かすゲーム")

# 色の定義
black = (0, 0, 0)

# 画像の読み込み
image = pygame.image.load("ex05/fig/invaders.png")  # 画像ファイルのパスに適宜変更してください
beam_image = pygame.image.load("ex05/fig/beam.png")  # ビーム画像のパスに適宜変更してください

# Playerオブジェクトの作成
player = Player(image, window_width // 2, window_height - image.get_height() // 2 - 10, 5)

# 敵の作成
enemy_image = pygame.image.load("ex05/fig/explosion.gif")  # 敵画像ファイルのパスに適宜変更してください
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = window_width // 2
enemy_rect.centery = window_height // 2

# スプライトグループの作成とプレイヤーの追加
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# ビームのスプライトグループの作成
beams = pygame.sprite.Group()

# ゲームループ
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # フレームレートを60に設定

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # スプライトグループの更新
    all_sprites.update()

    # 背景を描画
    window.fill(black)

    # 敵を描画
    window.blit(enemy_image, enemy_rect)

    # スプライトグループの描画
    all_sprites.draw(window)

    # ゲームウィンドウを更新
    pygame.display.update()

# ゲームの終了
pygame.quit()
