import pygame
pygame.init()


info_object = pygame.display.Info()
computer_width_res = info_object.current_w - 100
computer_height_res = info_object.current_h - 100


# Background Image
position = (0, 0)
game_play_bg = pygame.image.load("./../GameImageStored/GamePlay.png")


def back_ground_image_game_play(image_game_play, game_screen_size):
    game_play_bg_size = pygame.transform.scale(image_game_play, (computer_width_res, computer_height_res))
    game_screen_size.blit(game_play_bg_size, (0, 0))


def user_play(game_screen_size):
    play = True
    while play:
        back_ground_image_game_play(game_play_bg, game_screen_size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
