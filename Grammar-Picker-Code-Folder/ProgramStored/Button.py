import os
import pygame

pygame.init()


font_path = os.path.join('./../FontText/TextFont.ttf')


class MainMenuBtn:
    def __init__(self, x, y, image, btn_scale, image_hover):
        width = image.get_width()
        height = image.get_height()
        btn_width = int(width * btn_scale)
        btn_height = int(height * btn_scale)
        self.img = pygame.transform.scale(image, (btn_width, btn_height))
        self.img_hover = pygame.transform.scale(image_hover, (btn_width, btn_height))
        self.img_rect = self.img.get_rect()
        self.img_hover_rect = self.img_hover.get_rect()
        self.img_rect.topleft = ((x - btn_width) / 2, y)
        self.btn_clicked = False

    def play_btn(self, surface):
        action = False
        mouse_hover = False
        mouse_pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.img_rect.collidepoint(mouse_pos):
            mouse_hover = True
            if pygame.mouse.get_pressed()[0] == 1 and self.btn_clicked is False:
                self.btn_clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.btn_clicked = False

        if mouse_hover:
            surface.blit(self.img_hover, (self.img_rect.x, self.img_rect.y))
        else:
            surface.blit(self.img, (self.img_rect.x, self.img_rect.y))

        return [action, mouse_hover]


class AnswerButton:
    def __init__(self, loc_x, loc_y, screen_width, screen_height):
        self.btn_ans_x = screen_width * (loc_x / 100)
        self.btn_ans_y = screen_height * (loc_y / 100)
        self.btn_size = (screen_width + screen_height) * 0.07

    def player_one_btn_draw(self, surface_draw, animation_arr, index, text_choice, penalty):
        scale_image = pygame.transform.scale(animation_arr[index], (self.btn_size, self.btn_size))
        surface_draw.blit(scale_image, (self.btn_ans_x, self.btn_ans_y))

        if penalty[1] is True:
            text_choice = ""

        if penalty[0] is False:
            text = text_choice

            max_width = self.btn_size * 0.80
            base_font_size = 25
            font = pygame.font.Font(font_path, base_font_size)
            text_width, text_height = font.size(text)

            while text_width > max_width:
                base_font_size -= 1
                font = pygame.font.Font(font_path, base_font_size)
                text_width, text_height = font.size(text)

            text_surface = font.render(text, True, (0, 0, 0))

            center_x = (self.btn_ans_x + (self.btn_size - text_width) / 2) + 10
            center_y = (self.btn_ans_y + (self.btn_size - text_height) / 2) + 10

            surface_draw.blit(text_surface, (center_x, center_y))

        player_pressed_keys = pygame.key.get_pressed()
        player_one_key_map = {
            pygame.K_q: "Q",
            pygame.K_w: "W",
            pygame.K_e: "E",
            pygame.K_r: "R",
        }

        for key, value in player_one_key_map.items():
            if player_pressed_keys[key]:
                return value

    def player_two_btn_draw(self, surface_draw, animation_arr, index, text_choice, penalty):
        scale_image = pygame.transform.scale(animation_arr[index], (self.btn_size, self.btn_size))
        surface_draw.blit(scale_image, (self.btn_ans_x, self.btn_ans_y))

        if penalty[1] is True:
            text_choice = ""

        if penalty[0] is False:
            text = text_choice

            max_width = self.btn_size * 0.80
            base_font_size = 25
            font = pygame.font.Font(font_path, base_font_size)
            text_width, text_height = font.size(text)

            while text_width > max_width:
                base_font_size -= 1
                font = pygame.font.Font(font_path, base_font_size)
                text_width, text_height = font.size(text)

            text_surface = font.render(text, True, (0, 0, 0))

            center_x = (self.btn_ans_x + (self.btn_size - text_width) / 2) + 10
            center_y = (self.btn_ans_y + (self.btn_size - text_height) / 2) + 10

            surface_draw.blit(text_surface, (center_x, center_y))

        player_pressed_keys = pygame.key.get_pressed()
        player_two_key_map = {
            pygame.K_KP1: 1,
            pygame.K_KP2: 2,
            pygame.K_KP3: 3,
            pygame.K_KP4: 4
        }

        for key, value in player_two_key_map.items():
            if player_pressed_keys[key]:
                return value


class ButtonWinner:
    def __init__(self, x, y, image, btn_scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * btn_scale), int(height * btn_scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.btn_clicked = False

    def after_win_btn(self, surface):
        action = False
        mouse_hover = False

        mouse_pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            mouse_hover = True

            if pygame.mouse.get_pressed()[0] == 1 and self.btn_clicked is False:
                self.btn_clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.btn_clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return [action, mouse_hover]