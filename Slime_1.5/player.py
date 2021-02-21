from pygame.sprite import Sprite, collide_rect
from pygame import Surface, mixer
import pyganim

mixer.pre_init(44100, -16, 1, 512)
mixer.init()

MOVE_SPEED = 2
JUMP_POWER = 10
G = 1
COLOR = (200, 200, 200)

ANIMATION_DELAY = 180
ANIMATION_STAY = [('image/user/user_0.png', ANIMATION_DELAY), ('image/user/user_1.png', ANIMATION_DELAY),
                  ('image/user/user_2.png', ANIMATION_DELAY), ('image/user/user_3.png', ANIMATION_DELAY),
                  ('image/user/user_4.png', ANIMATION_DELAY)]

ANIMATION_RIGHT = [('image/user/user_r_0.png', ANIMATION_DELAY), ('image/user/user_r_1.png', ANIMATION_DELAY),
                   ('image/user/user_r_2.png', ANIMATION_DELAY), ('image/user/user_r_3.png', ANIMATION_DELAY),
                   ('image/user/user_r_4.png', ANIMATION_DELAY), ('image/user/user_r_5.png', ANIMATION_DELAY)]

ANIMATION_LEFT = [('image/user/user_l_0.png', ANIMATION_DELAY), ('image/user/user_l_1.png', ANIMATION_DELAY),
                  ('image/user/user_l_2.png', ANIMATION_DELAY), ('image/user/user_l_3.png', ANIMATION_DELAY),
                  ('image/user/user_l_4.png', ANIMATION_DELAY), ('image/user/user_l_5.png', ANIMATION_DELAY)]


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.y_vel = 0
        self.x_vel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.underground = False

        self.boltAnimationStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimationStay.play()

        self.boltAnimationRight = pyganim.PygAnimation(ANIMATION_RIGHT)
        self.boltAnimationRight.play()

        self.boltAnimationLeft = pyganim.PygAnimation(ANIMATION_LEFT)
        self.boltAnimationLeft.play()

        self.jump_sound = mixer.Sound('sound/jump.ogg')
        self.magma_sound = mixer.Sound('sound/magma.ogg')

        self.level = 1

        self.hp = 12

    def update(self, left, right, up, platforms, portals, magmas):
        if self.hp <= 0:
            self.level = 1
            self.hp = 12

        if left:
            self.x_vel = -MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimationLeft.blit(self.image, (0, 0))

        if right:
            self.x_vel = MOVE_SPEED
            self.image.fill(COLOR)
            self.boltAnimationRight.blit(self.image, (0, 0))

        if up:
            if self.underground:
                self.y_vel = -JUMP_POWER
                self.jump_sound.play()

        if not (left or right):
            self.x_vel = 0
            if not up:
                self.image.fill(COLOR)
                self.boltAnimationStay.blit(self.image, (0, 0))

        if not self.underground:
            self.y_vel += G

        self.underground = False
        self.rect.x += self.x_vel
        self.collide(self.x_vel, 0, platforms, portals, magmas)
        self.rect.y += self.y_vel
        self.collide(0, self.y_vel, platforms, portals, magmas)

    def collide(self, x_vel, y_vel, platforms, portals, magmas):
        global JUMP_POWER
        for pl in platforms:
            if collide_rect(self, pl):
                if x_vel > 0:
                    self.rect.right = pl.rect.left
                if x_vel < 0:
                    self.rect.left = pl.rect.right
                if y_vel > 0:
                    self.rect.bottom = pl.rect.top
                    self.underground = True
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = pl.rect.bottom
                if JUMP_POWER != 10:
                    JUMP_POWER = 10

        for pr in portals:
            if collide_rect(self, pr):
                if x_vel > 0:
                    self.rect.right = pr.rect.left
                    self.level += 1
                if x_vel < 0:
                    self.rect.left = pr.rect.right
                    self.level += 1
                if y_vel > 0:
                    self.rect.bottom = pr.rect.top
                    self.underground = True
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = pr.rect.bottom

        for mg in magmas:
            if collide_rect(self, mg):
                if x_vel > 0:
                    self.rect.right = mg.rect.left
                if x_vel < 0:
                    self.rect.left = mg.rect.right
                if y_vel > 0:
                    self.rect.bottom = mg.rect.top
                    self.underground = True
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = mg.rect.bottom
                if JUMP_POWER != 6:
                    JUMP_POWER = 6
                self.magma_sound.play()
                self.hp -= 1
