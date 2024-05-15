import pygame
import Button
from GamePlay import user_play
from pygame import mixer

pygame.init()

info_object = pygame.display.Info()
computer_width_res = info_object.current_w - 100  # 1340
computer_height_res = info_object.current_h - 100  # 800
game_screen_size = pygame.display.set_mode((computer_width_res, computer_height_res))

main_menu_bg_clr = (255, 255, 255)
position = (0, 0)
main_menu_bg = pygame.image.load("./../GameImageStored/MainMenuBG.png")

# Load button image
play_menu = pygame.image.load("./../GameImageStored/play_menu_btn.png").convert_alpha()
play_menu_hover = pygame.image.load("./../GameImageStored/play_menu_btn_hover.png").convert_alpha()
exit_menu = pygame.image.load("./../GameImageStored/exit_menu_btn.png").convert_alpha()
exit_menu_hover = pygame.image.load("./../GameImageStored/exit_menu_btn_hover.png").convert_alpha()

# Create button instances
play_button = Button.Button(computer_width_res * 0.40, computer_height_res * 0.35, play_menu, 0.8, play_menu_hover)
exit_button = Button.Button(computer_width_res * 0.40, computer_height_res * 0.5, exit_menu, 0.8, exit_menu_hover)


def back_ground_image_menu(image_menu):
    game_bg_size = pygame.transform.scale(image_menu, (computer_width_res, computer_height_res))
    game_screen_size.blit(game_bg_size, (0, 0))


# Background Music
mixer.music.load("./../GameMusicStored/MainMenuBgMusic.mp3")
mixer.music.play(-1)

# Click Sound Effect
click_sound_effect = mixer.Sound("./../GameMusicStored/Click.mp3")


def main_menu():
    pygame.display.set_caption("Menu")
    running = True
    while running:
        game_screen_size.fill(main_menu_bg_clr)
        back_ground_image_menu(main_menu_bg)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if play_button.draw_btn(game_screen_size)[0]:
            click_sound_effect.play()
            mixer.music.stop()
            user_play(game_screen_size, computer_width_res, computer_height_res)
            running = False

        if exit_button.draw_btn(game_screen_size)[0]:
            click_sound_effect.play()
            pygame.time.delay(500)
            running = False

        if play_button.draw_btn(game_screen_size)[1] or exit_button.draw_btn(game_screen_size)[1]:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.update()


main_menu()
