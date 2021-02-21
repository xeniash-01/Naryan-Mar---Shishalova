import pygame
from player import Player
from Platform import Platform

SIZE = (800, 600)

LEVEL = 1

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('SlImE')

icon = pygame.image.load('image/icon/icon.png')
pygame.display.set_icon(icon)

screen = pygame.Surface(SIZE)

clock = pygame.time.Clock()

# hero==================================================================================================================

hero = Player(20, 760)
left = right = up = False

# hp====================================================================================================================

hp = pygame.image.load('image/interface/hp.png')

run_button_1 = pygame.image.load('image/interface/run_1.png')
run_button_2 = pygame.image.load('image/interface/run_2.png')

out_button_1 = pygame.image.load('image/interface/out_1.png')
out_button_2 = pygame.image.load('image/interface/out_2.png')

continue_button_1 = pygame.image.load('image/interface/continue_1.png')
continue_button_2 = pygame.image.load('image/interface/continue_2.png')

fon = pygame.image.load('image/interface/fon.png')

point = pygame.image.load('image/interface/point.png')

no_point = pygame.image.load('image/interface/no_point.png')

# level=================================================================================================================

p = [True, True, True, True, True]

level_1 = [
    '5888888888888888888888888888888888888888888888888888885',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6 t     tt                                            4',
    '6 t      t                                            4',
    '6 t      t                                            4',
    '6 t      t                                            4',
    '6 ttt t ttt                                           4',
    '6                                         122222223   4',
    '6                                      13 455555556   4',
    '6                                         45555556    4',
    '6                                  123    45555556    4',
    '6                                       125555556     4',
    '6                             13        455555556     4',
    '6                        13             45555556      4',
    '6                  123                 155555556      4',
    '6                                      45555555p      4',
    '6             13                       45555555       4',
    '6                                     15555555553     4',
    '6         13                          455555555553    4',
    '6                                     4555555555553   4',
    '5222222222222222222222222222222222222255555555555552225'
]

level_2 = [
    '5888888888888888888888888888888888888888888888888888885',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                              123    4',
    '6                                                     4',
    '6                                        1223         4',
    '6                                                     4',
    '6                                 1223                4',
    '6                                                     4',
    '6                                        123        125',
    '6                                                     4',
    '6                                   123               4',
    '6 t     ttt                                           4',
    '6 t       t                              13           4',
    '6 t      t                                            4',
    '6 t     t                           123            1225',
    '6 ttt t ttt                                           4',
    '6                             123                     4',
    '6                                                     4',
    '6                        123                          4',
    '6                                                     4',
    '6                  123                                4',
    '6                                                     4',
    '6                        13                           4',
    '6                             13                      4',
    '6                                              13     4',
    '6                         13                          4',
    '6                                                     p',
    '6                    123                               ',
    '52222222222222222222255522222222                   2225',
    '55555555555555555555555555555555mmmmmmmmmmmmmmmmmmm5555'
]

level_3 = [
    '5888888888888888888888888888888888888888888888888888885',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6 t     ttt                                           4',
    '6 t       t                                           4',
    '6 t      t                                            4',
    '6 t       t                                           4',
    '6 ttt t ttt       12223                               4',
    '6             13                                      4',
    '6         13                                          4',
    '6    13                                               4',
    '6                                                     4',
    '523                                                   4',
    '6                                                     4',
    '6    13                                               4',
    '6                                                     4',
    '6      13   1223                                      4',
    '6                                                     4',
    '6                 13                                  p',
    '6                                                      ',
    '522222222   22222222     2222    22222   222    22   25',
    '555555555mmm55555555mmmmm5555mmmm55555mmm555mmmm55mmm55'
]

level_4 = [
    '5888888888888888888888888888888888888888888888888888885',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6                                                     4',
    '6          t t  tt  t  t  t t t ttt t  t              4',
    '6          t t t  t t  t  t t t  t  tt t              4',
    '6          ttt t  t t  t  t t t  t  t tt              4',
    '6           t  t  t t  t  t t t  t  t  t              4',
    '6           t   tt   tt    t t  ttt t  t              4',
    '6                                                     4',
    '6 p     p     p      p      p     p     p     p     p 4',
    '6                                                     4',
    '6 p     p     p      p      p     p     p     p     p 4',
    '6                                                     4',
    '5222222222222222222222222222222222222222222222222222225'
]


class Level:
    def __init__(self, level, x, y, num):
        self.level = level
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(hero)
        self.platforms = []
        self.portals = []
        self.magmas = []
        self.x = x
        self.y = y

        self.num = num

    def make_level(self):
        x, y = 0, 0
        for row in self.level:
            for col in row:
                if col == '1':
                    block_1 = Platform(x, y, 'image/platform/block_1_ul.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '2':
                    block_1 = Platform(x, y, 'image/platform/block_1_u.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '3':
                    block_1 = Platform(x, y, 'image/platform/block_1_ur.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '4':
                    block_1 = Platform(x, y, 'image/platform/block_1_cl.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '5':
                    block_1 = Platform(x, y, 'image/platform/block_1_c.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '6':
                    block_1 = Platform(x, y, 'image/platform/block_1_cr.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '7':
                    block_1 = Platform(x, y, 'image/platform/block_1_dl.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '8':
                    block_1 = Platform(x, y, 'image/platform/block_1_d.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == '9':
                    block_1 = Platform(x, y, 'image/platform/block_1_dr.png')
                    self.sprite_group.add(block_1)
                    self.platforms.append(block_1)
                elif col == 'p':
                    block_1 = Platform(x, y, 'image/platform/portal_1.png')
                    self.sprite_group.add(block_1)
                    self.portals.append(block_1)
                elif col == 'm':
                    block_1 = Platform(x, y, 'image/platform/magma.png')
                    self.sprite_group.add(block_1)
                    self.magmas.append(block_1)
                elif col == 't':
                    block_1 = Platform(x, y, 'image/platform/text.png')
                    self.sprite_group.add(block_1)
                x += 20
            y += 20
            x = 0

    def start(self):
        global game, menu, pause, hero, left, right, up

        pygame.mouse.set_visible(False)

        if p[self.num - 1]:
            hero.rect.x = self.x
            hero.rect.y = self.y
            left = right = up = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right = True
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    left = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    right = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    up = False

        screen.fill((200, 200, 200))

        # make hero=====================================================================================================

        hero.update(left, right, up, self.platforms, self.portals, self.magmas)
        camera.update(hero)
        for e in self.sprite_group:
            screen.blit(e.image, camera.apply(e))

        window.blit(screen, (0, 0))

        for i in range(hero.hp):
            window.blit(hp, (i * 14 + 5, 5))

        pygame.display.flip()

        clock.tick(60)


# menu==================================================================================================================

menu = True


def start_menu():
    global menu, game, pause, LEVEL, left, right, up

    if menu:
        left = right = up = False
        pygame.mouse.set_visible(True)
        LEVEL = 0
        hero.level = 1
        hero.hp = 12

    if 500 >= pygame.mouse.get_pos()[0] >= 300 and 220 >= pygame.mouse.get_pos()[1] >= 150:
        run_button = run_button_2
    else:
        run_button = run_button_1

    if 500 >= pygame.mouse.get_pos()[0] >= 300 and 370 >= pygame.mouse.get_pos()[1] >= 300:
        out_button = out_button_2
    else:
        out_button = out_button_1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            game = False
            LEVEL = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 500 >= pygame.mouse.get_pos()[0] >= 300 and 220 >= pygame.mouse.get_pos()[1] >= 150:
                    menu = False
                    pause = False

            if event.button == 1:
                if 500 >= pygame.mouse.get_pos()[0] >= 300 and 370 >= pygame.mouse.get_pos()[1] >= 300:
                    menu = False
                    game = False
                    LEVEL = 0

    screen.fill((46, 63, 25))

    window.blit(screen, (0, 0))

    window.blit(run_button, (300, 150))

    window.blit(out_button, (300, 300))

    pygame.display.flip()

    clock.tick(60)


# pause=================================================================================================================

pause = False


def start_pause():
    global menu, game, pause, left, right, up

    left = right = up = False

    pygame.mouse.set_visible(True)

    while pause:
        if 630 >= pygame.mouse.get_pos()[0] >= 170 and 210 >= pygame.mouse.get_pos()[1] >= 150:
            continue_button = continue_button_2
        else:
            continue_button = continue_button_1

        if 500 >= pygame.mouse.get_pos()[0] >= 300 and 370 >= pygame.mouse.get_pos()[1] >= 300:
            out_button = out_button_2
        else:
            out_button = out_button_1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                game = False
                pause = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 630 >= pygame.mouse.get_pos()[0] >= 170 and 210 >= pygame.mouse.get_pos()[1] >= 150:
                        pause = False

                if event.button == 1:
                    if 500 >= pygame.mouse.get_pos()[0] >= 300 and 370 >= pygame.mouse.get_pos()[1] >= 300:
                        pause = False
                        menu = True

        screen.fill((46, 63, 25))
        window.blit(screen, (0, 0))

        window.blit(continue_button, (170, 150))

        window.blit(out_button, (300, 300))

        pygame.display.flip()
        clock.tick(60)


count = 0


def win_menu():
    global game, LEVEL, menu, count

    pygame.mouse.set_visible(True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            game = False
            LEVEL = 0

    if count < ((hero.hp // 2) + (hero.hp % 2)):
        window.blit(point, (count * 40 + 280, 250))
        count += 1

    if count == ((hero.hp // 2) + (hero.hp % 2)):
        for i in range(((hero.hp // 2) + (hero.hp % 2))):
            window.blit(point, (i * 40 + 280, 250))

    for i in range(6):
        window.blit(no_point, (i * 40 + 280, 250))

    window.blit(fon, (0, 0))

    pygame.display.flip()
    clock.tick(30)


# camera================================================================================================================


class Camera:
    def __init__(self, c_f, width, height):
        self.c_f = c_f
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.c_f(self.state, target.rect)


def camera_func(c, target_rect):
    k = -target_rect.x + SIZE[0] / 2
    t = -target_rect.y + SIZE[1] / 2
    w, h = c.width, c.height

    k = min(0, k)
    k = max(-(c.width - SIZE[0]), k)
    t = max(-(c.height - SIZE[1]), t)
    t = min(0, t)

    return pygame.Rect(k, t, w, h)


total_level_width = len(level_1[0]) * 20
total_level_height = len(level_1) * 20

camera = Camera(camera_func, total_level_width, total_level_height)

# sound=================================================================================================================

# pygame.mixer.pre_init(44100, -16, 1, 512)
# pygame.mixer.init()
# sound = pygame.mixer.Sound('sound/fon.ogg')
# sound.play(-1)

# run_level==============================================================================================================

game = True

Level_1 = Level(level_1, 40, 700, 1)
Level_1.make_level()

Level_2 = Level(level_2, 40, 700, 2)
Level_2.make_level()

Level_3 = Level(level_3, 40, 700, 3)
Level_3.make_level()

Level_4 = Level(level_4, 480, 20, 4)
Level_4.make_level()

# run_game==============================================================================================================

while game:
    if menu:
        start_menu()
    else:
        LEVEL = hero.level

    if LEVEL == 1:
        Level_1.start()
    elif LEVEL == 2:
        Level_2.start()
    elif LEVEL == 3:
        Level_3.start()
    elif LEVEL == 4:
        Level_4.start()
    elif LEVEL == 5:
        win_menu()

    if pause:
        start_pause()

    p = [True] * 5
    p[LEVEL - 1] = False
