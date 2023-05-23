import pygame

# Playerクラス
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

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

# Playerオブジェクトの作成
player = Player(image, window_width // 2, window_height - image.get_height() // 2 - 10, 5)

# 敵の作成
enemy_image = pygame.image.load("ex05/fig/explosion.gif")  # 敵画像ファイルのパスに適宜変更してください
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = window_width // 2
enemy_rect.centery = window_height // 2

# スプライトグループの作成と敵の追加
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

    # スプライトグループの描画
    all_sprites.draw(window)

    # 敵を描画
    window.blit(enemy_image, enemy_rect)

    # ゲームウィンドウを更新
    pygame.display.update()

# ゲームの終了
pygame.quit()
