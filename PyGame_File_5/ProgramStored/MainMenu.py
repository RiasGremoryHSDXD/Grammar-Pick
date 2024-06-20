import os.path
import Button
import pygame
from LoadingAnimation import loading_ani
from pygame import mixer


pygame.init()

width_screen = 1200
height_screen = 700
screen = pygame.display.set_mode((width_screen, height_screen))
alpha = 0


# Game title
menu_title = pygame.image.load("./../ImageStored/MainMenuTitle.png")
menu_bg = pygame.image.load("./../ImageStored/MainMenuBG.png")
menu_sz = pygame.transform.scale(menu_bg, (width_screen, height_screen))

# Game Main Menu Button
play_btn = pygame.image.load("./../ImageStored/play_btn.png")
play_btn_hover = pygame.image.load("./../ImageStored/play_btn_hover.png")
exit_btn = pygame.image.load("./../ImageStored/exit_btn.png")
exit_btn_hover = pygame.image.load("./../ImageStored/exit_btn_hover.png")

# Background Player 1
ply_one_bg = pygame.image.load("./../ImageStored/Player_1_BG.png")
ply_one_size = pygame.transform.scale(ply_one_bg, (width_screen, height_screen))

# Background Player 2
ply_two_bg = pygame.image.load("./../ImageStored/Player_2_BG.png")
ply_two_size = pygame.transform.scale(ply_two_bg, (width_screen, height_screen))

# Game Icon
icon = pygame.image.load("./../ImageStored/GameIconLogo.png")
pygame.display.set_icon(icon)


# Player 1 Run motion
ply_one_ani = [None] * 8
for picIndex in range(1, 9):
    image = pygame.image.load(os.path.join("./../ImageStored/WizardRunMotion/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 100))
    ply_one_ani[picIndex - 1] = scaled_image

# Player 2 Run motion
ply_two_ani = [None] * 8
for picIndex in range(1, 9):
    image = pygame.image.load(os.path.join("./../ImageStored/LadyRunMotion/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 100))
    ply_two_ani[picIndex - 1] = scaled_image

# Portal Animation
portal = [None] * 3
for picIndex in range(1, 4):
    image = pygame.image.load(os.path.join("./../ImageStored/Portal/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 150))
    portal[picIndex - 1] = scaled_image

# Music
mixer.music.load("./../MusicStored/BG_music.mp3")
mixer.music.play(-1)

click_sound_effect = mixer.Sound("./../MusicStored/Click.mp3")
portal_effect = mixer.Sound("./../MusicStored/Portal_SE.mp3")
portal_effect.set_volume(0.15)


class MoveCharacter:

    def __init__(self, draw_screen, scr_wid, scr_hei):
        self.screen_draw = draw_screen
        self.scr_wid = scr_wid
        self.scr_hei = scr_hei
        self.stepIndex = 0
        self.PortalAni = 0
        self.ply_one_x = 0
        self.ply_two_x = scr_wid - 100
        self.ply_one_y = scr_hei * 0.78
        self.ply_two_y = scr_hei * 0.30
        self.last_update = pygame.time.get_ticks()
        self.last_update_portal = pygame.time.get_ticks()
        self.one_bg_x = 0
        self.two_bg_x = 0

    def character_run(self):

        current_time = pygame.time.get_ticks()
        if self.stepIndex >= 8:
            self.stepIndex = 0

        if current_time - self.last_update >= 50:
            self.last_update = current_time
            self.stepIndex += 1

        self.one_bg_img()
        self.two_bg_img()
        self.screen_draw.blit(ply_one_ani[self.stepIndex//2], (self.ply_one_x, self.ply_one_y))
        self.screen_draw.blit(ply_two_ani[self.stepIndex//2], (self.ply_two_x, self.ply_two_y))

    def character_portal(self):

        self.screen_draw.blit(menu_sz, (0, 0))
        mixer.music.stop()
        self.portal()
        portal_effect.play()
        current_time = pygame.time.get_ticks()
        if self.stepIndex >= 8:
            self.stepIndex = 0

        if current_time - self.last_update >= 50:
            self.last_update = current_time
            self.stepIndex += 1

        self.ply_one_x += 3
        self.ply_two_x -= 3

        if self.ply_one_x > self.scr_wid or self.ply_two_x < 0:
            portal_effect.stop()
            loading_ani(self.screen_draw, self.scr_wid, self.scr_hei)

        self.screen_draw.blit(ply_one_ani[self.stepIndex//2], (self.ply_one_x, self.ply_one_y))
        self.screen_draw.blit(ply_two_ani[self.stepIndex//2], (self.ply_two_x, self.ply_two_y))

    def portal(self):
        current_time = pygame.time.get_ticks()

        if self.PortalAni >= 4:
            self.PortalAni = 0

        if current_time - self.last_update_portal >= 50:
            self.last_update_portal = current_time
            self.PortalAni += 1

        self.screen_draw.blit(portal[self.PortalAni // 2], (self.scr_wid * 0.90, self.ply_one_y - 50))
        self.screen_draw.blit(portal[self.PortalAni // 2], (10, self.ply_two_y - 50))

    def one_bg_img(self):
        self.screen_draw.blit(ply_one_size, (self.one_bg_x, self.scr_hei / 2))
        self.screen_draw.blit(ply_one_size, (self.scr_wid + self.one_bg_x, self.scr_hei / 2))

        self.one_bg_x -= 3
        if self.one_bg_x <= -self.scr_wid:
            self.one_bg_x = 0

    def two_bg_img(self):
        self.screen_draw.blit(ply_two_size, (self.two_bg_x, -(self.scr_hei / 2)))
        self.screen_draw.blit(ply_two_size, (self.two_bg_x - self.scr_wid, -(self.scr_hei / 2)))

        self.two_bg_x += 3
        if self.two_bg_x >= self.scr_wid:
            self.two_bg_x = 0


def game_title():
    menu_wid = width_screen * 0.5
    menu_hei = 60
    menu_title_size = pygame.transform.scale(menu_title, (menu_wid, menu_hei))
    screen.blit(menu_title_size, ((width_screen - menu_wid) * 0.5, (height_screen - menu_hei) * 0.2))


def dark_envi(transparency):
    dark_surface = pygame.Surface((width_screen, height_screen))
    dark_surface.set_alpha(transparency)
    dark_surface.fill((0, 0, 0))
    screen.blit(dark_surface, (0, 0))


ply_move_ani = MoveCharacter(screen, width_screen, height_screen)
play_btn_cls = Button.MainMenuBtn(width_screen, height_screen * 0.35, play_btn, 2, play_btn_hover)
exit_btn_cls = Button.MainMenuBtn(width_screen, height_screen * 0.55, exit_btn, 2, exit_btn_hover)

click_ply_btn = False
fade_in = True
play_stage = False
run = True
while run:
    pygame.display.set_caption("Menu")

    if play_stage is False:
        ply_move_ani.character_run()
    else:
        ply_move_ani.character_portal()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not play_stage:
        if not click_ply_btn:
            game_title()

            if play_btn_cls.play_btn(screen)[0] and not click_ply_btn:
                click_sound_effect.play()
                click_ply_btn = True
            if exit_btn_cls.play_btn(screen)[0] and not click_ply_btn:
                click_sound_effect.play()
                pygame.time.delay(100)
                run = False

            if (play_btn_cls.play_btn(screen)[1] or exit_btn_cls.play_btn(screen)[1]) and not click_ply_btn:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    else:
        pass

    if click_ply_btn:
        if fade_in:
            if alpha < 255:
                alpha += 4.5  # Adjust this value to control the speed of the fade
            else:
                fade_in = False
        else:
            if alpha > 0:
                alpha -= 1
            else:
                play_stage = True
        dark_envi(alpha)

    pygame.display.update()

pygame.quit()
