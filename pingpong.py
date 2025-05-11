from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 200: 
            self.rect.y += self.speed
    def update_p(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 180: 
            self.rect.y += self.speed
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
BACK = (200, 255, 255)
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
FPS = 60

player_p = Player("rocket P.png", 30, 200, 5, 50, 200)
player_l = Player("rocket L.png", 520, 200, 5, 50, 200)
boll = GameSprite("boll.png", 200, 200, 5, 50, 50)

speed_x = boll.speed
speed_y = boll.speed


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(BACK)

        boll.rect.x += speed_x
        boll.rect.y += speed_y

        player_p.update_p()
        player_l.update_l()


        if boll.rect.y > win_height - 50 or boll.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_l, boll)  or sprite.collide_rect(player_p, boll):
            speed_x *= -1

        player_l.reset()
        player_p.reset()

        boll.reset()




    display.update()
    clock.tick(FPS)
