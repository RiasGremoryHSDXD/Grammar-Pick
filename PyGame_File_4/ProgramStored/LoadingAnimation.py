import pygame
import sys
from PlayStage import play_stage
pygame.init()


def loading_ani(screen, width_screen, height_screen):
    menu_bg = pygame.image.load("./../ImageStored/MainMenuBG.png")
    menu_sz = pygame.transform.scale(menu_bg, (width_screen, height_screen))

    initial_loading_bar_width = 500
    initial_loading_bar_height = 30
    initial_bg_bar_width = initial_loading_bar_width + 20
    initial_bg_bar_height = initial_loading_bar_height + 20

    # Loading BG
    loading_bg = pygame.image.load("./../ImageStored/Loading Bar Background.png")
    loading_bg = pygame.transform.scale(loading_bg, (initial_bg_bar_width, initial_bg_bar_height))
    loading_bg_rect = loading_bg.get_rect(center=(640, 600))

    # Loading Bar and variables
    loading_bar = pygame.image.load("./../ImageStored/Loading Bar.png")
    loading_bar = pygame.transform.scale(loading_bar, (initial_loading_bar_width, initial_loading_bar_height))

    total_loading_time = 5000

    # Track the start time
    start_time = pygame.time.get_ticks()
    loading_finished = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(menu_sz, (0, 0))
        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time < total_loading_time:
            loading_bar_width = elapsed_time / total_loading_time * initial_loading_bar_width

            loading_bar_scaled = pygame.transform.scale(loading_bar,
                                                        (int(loading_bar_width), initial_loading_bar_height))
            loading_bar_rect = loading_bar_scaled.get_rect(midleft=(loading_bg_rect.left + 10, 600))

            screen.blit(loading_bg, loading_bg_rect)
            screen.blit(loading_bar_scaled, loading_bar_rect)
        else:
            if not loading_finished:
                play_stage(screen, width_screen, height_screen)

        pygame.display.update()
