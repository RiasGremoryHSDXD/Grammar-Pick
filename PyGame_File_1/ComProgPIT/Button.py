import pygame
pygame.init()


class Button:
    def __init__(self, x, y, image, btn_scale, image_hover):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * btn_scale), int(height * btn_scale)))
        self.image_hover = pygame.transform.scale(image_hover, (int(width * btn_scale), int(height * btn_scale)))
        self.rect = self.image.get_rect()
        self.image_hover_rec = self.image_hover.get_rect()
        self.rect.topleft = (x, y)
        self.image_hover_rec.topleft = (x, y)
        self.btn_clicked = False

    def draw_btn(self, surface):
        action = False
        mouse_hover = False
        mouse_pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            mouse_hover = True
            if pygame.mouse.get_pressed()[0] == 1 and self.btn_clicked == False:
                self.btn_clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.btn_clicked = False

        if mouse_hover:
            surface.blit(self.image_hover, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        return [action, mouse_hover]
