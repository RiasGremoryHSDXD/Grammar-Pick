import pygame
import os.path
import Button

pygame.init()

# Background Image
position = (0, 0)
game_play_bg = pygame.image.load("./../GameImageStored/GamePlayBG.png")

Q_animation = [None] * 6
for picIndex in range(1, 7):
    Q_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_Q/" + "btn_Q" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

W_animation = [None] * 6
for picIndex in range(1, 7):
    W_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_W/" + "btn_W" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

E_animation = [None] * 6
for picIndex in range(1, 7):
    E_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_E/" + "btn_E" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

R_animation = [None] * 6
for picIndex in range(1, 7):
    R_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_R/" + "btn_R" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

One_animation = [None] * 6
for picIndex in range(1, 7):
    One_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_1/" + "btn_1" + str(picIndex)
                                                                 + ".png"))
    picIndex += 1

Two_animation = [None] * 6
for picIndex in range(1, 7):
    Two_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_2/" + "btn_2" + str(picIndex)
                                                                 + ".png"))
    picIndex += 1

Three_animation = [None] * 6
for picIndex in range(1, 7):
    Three_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_3/" + "btn_3" +
                                                                   str(picIndex) + ".png"))
    picIndex += 1

Four_animation = [None] * 6
for picIndex in range(1, 7):
    Four_animation[picIndex - 1] = pygame.image.load(os.path.join("./../GameImageStored/btn_4/" + "btn_4" +
                                                                  str(picIndex) + ".png"))
    picIndex += 1


def user_play(game_screen_sizes, computer_width_res, computer_height_res):
    pygame.display.set_caption("Game Stage")

    def back_ground_image_game_play(image_game_play, game_screen_size_para):
        game_play_bg_size = pygame.transform.scale(image_game_play, (computer_width_res, computer_height_res))
        game_screen_size_para.blit(game_play_bg_size, (0, 0))

    ply_one_first_choice = Button.AnswerButton(10, 50, computer_width_res, computer_height_res)
    ply_one_second_choice = Button.AnswerButton(25, 50, computer_width_res, computer_height_res)
    ply_one_third_choice = Button.AnswerButton(10, 70, computer_width_res, computer_height_res)
    ply_one_fourth_choice = Button.AnswerButton(25, 70, computer_width_res, computer_height_res)

    ply_two_first_choice = Button.AnswerButton(65, 50, computer_width_res, computer_height_res)
    ply_two_second_choice = Button.AnswerButton(80, 50, computer_width_res, computer_height_res)
    ply_two_third_choice = Button.AnswerButton(65, 70, computer_width_res, computer_height_res)
    ply_two_fourth_choice = Button.AnswerButton(80, 70, computer_width_res, computer_height_res)

    class PlayerScore:

        def __init__(self, class_game_screen_sizes):
            self.player_one_score = 0
            self.player_two_score = 0
            self.player_one_choice = None
            self.player_two_choice = None
            self.player_one_arr_ans = ["Q", "W", "E", "R"]
            self.player_two_arr_ans = [1, 2, 3, 4]
            self.btn_color_one = (92, 255, 230)
            self.btn_color_two = (92, 255, 230)
            self.btn_color_pressed = (0, 0, 0)
            self.player_one_penalty = False
            self.player_two_penalty = False
            self.player_penalty_time = 0
            self.player_one_penalty_time = None
            self.player_two_penalty_time = None
            self.player_one_animation_count = 0
            self.player_two_animation_count = 0
            self.class_game_screen_size = class_game_screen_sizes

        def player_one_button(self):

            if (ply_one_first_choice.player_one_btn_draw(self.class_game_screen_size, Q_animation,
                                                         self.player_one_animation_count) ==
                    "Q"):
                self.player_one_choice = ply_one_first_choice.player_one_btn_draw(self.class_game_screen_size,
                                                                                  Q_animation,
                                                                                  self.player_one_animation_count)
            if (ply_one_second_choice.player_one_btn_draw(self.class_game_screen_size, W_animation,
                                                          self.player_one_animation_count) ==
                    "W"):
                self.player_one_choice = ply_one_second_choice.player_one_btn_draw(self.class_game_screen_size,
                                                                                   W_animation,
                                                                                   self.player_one_animation_count)
            if (ply_one_third_choice.player_one_btn_draw(self.class_game_screen_size, E_animation,
                                                         self.player_one_animation_count) ==
                    "E"):
                self.player_one_choice = ply_one_third_choice.player_one_btn_draw(self.class_game_screen_size,
                                                                                  E_animation,
                                                                                  self.player_one_animation_count)
            if (ply_one_fourth_choice.player_one_btn_draw(self.class_game_screen_size, R_animation,
                                                          self.player_one_animation_count) ==
                    "R"):
                self.player_one_choice = ply_one_fourth_choice.player_one_btn_draw(self.class_game_screen_size,
                                                                                   R_animation,
                                                                                   self.player_one_animation_count)

            if self.player_one_choice is not None and self.player_one_choice in self.player_one_arr_ans:
                player_one_convert = self.player_one_arr_ans.index(self.player_one_choice)
                self.player_one_choice = ["A", "B", "C", "D"]
                self.player_one_choice = self.player_one_choice[player_one_convert]
                return self.player_one_choice

            return self.player_two_choice

        def player_two_button(self):

            if self.player_two_penalty:
                self.btn_color_two = (255, 255, 255)
            else:
                self.btn_color_two = (92, 255, 230)

            if (ply_two_first_choice.player_two_btn_draw(self.class_game_screen_size, One_animation,
                                                         self.player_two_animation_count)
                    == 1):
                self.player_two_choice = ply_two_first_choice.player_two_btn_draw(self.class_game_screen_size,
                                                                                  One_animation,
                                                                                  self.player_two_animation_count)
            if (ply_two_second_choice.player_two_btn_draw(self.class_game_screen_size, Two_animation,
                                                          self.player_two_animation_count)
                    == 2):
                self.player_two_choice = ply_two_second_choice.player_two_btn_draw(self.class_game_screen_size,
                                                                                   Two_animation,
                                                                                   self.player_two_animation_count)
            if (ply_two_third_choice.player_two_btn_draw(self.class_game_screen_size, Three_animation,
                                                         self.player_two_animation_count)
                    == 3):
                self.player_two_choice = ply_two_third_choice.player_two_btn_draw(self.class_game_screen_size,
                                                                                  Three_animation,
                                                                                  self.player_two_animation_count)
            if (ply_two_fourth_choice.player_two_btn_draw(self.class_game_screen_size, Four_animation,
                                                          self.player_two_animation_count)
                    == 4):
                self.player_two_choice = ply_two_fourth_choice.player_two_btn_draw(self.class_game_screen_size,
                                                                                   Four_animation,
                                                                                   self.player_two_animation_count)

            if self.player_two_choice is not None and self.player_two_choice in self.player_two_arr_ans:
                player_two_convert = self.player_two_arr_ans.index(self.player_two_choice)
                self.player_two_choice = ["A", "B", "C", "D"]
                self.player_two_choice = self.player_two_choice[player_two_convert]
                return self.player_two_choice

            return self.player_two_choice

        def players_time_penalty(self):
            if self.player_one_penalty is True:
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 100:
                    self.player_one_animation_count = 1
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 1500:
                    self.player_one_animation_count = 2
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 2700:
                    self.player_one_animation_count = 3
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 4000:
                    self.player_one_animation_count = 4
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 5000:
                    self.player_one_animation_count = 5
                if pygame.time.get_ticks() - self.player_one_penalty_time >= 6000:
                    self.player_one_animation_count = 0
                    self.player_one_penalty = False
            if self.player_two_penalty is True:
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 100:
                    self.player_two_animation_count = 1
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 1500:
                    self.player_two_animation_count = 2
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 2700:
                    self.player_two_animation_count = 3
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 4000:
                    self.player_two_animation_count = 4
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 5000:
                    self.player_two_animation_count = 5
                if pygame.time.get_ticks() - self.player_two_penalty_time >= 6000:
                    self.player_two_animation_count = 0
                    self.player_two_penalty = False

        def validate_answer(self, hot_keys_press):
            correct_answer = "A"
            player_one_answer = ply_draw_btn.player_one_button()
            player_two_answer = ply_draw_btn.player_two_button()
            self.players_time_penalty()

            if hot_keys_press:
                if player_one_answer == correct_answer and self.player_one_penalty is False:
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.player_two_animation_count = 0
                    self.player_one_score += 1
                if player_two_answer == correct_answer and self.player_two_penalty is False:
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.player_two_animation_count = 0
                    self.player_two_score += 1
                if (player_one_answer is not correct_answer and self.player_one_choice is not None and
                        self.player_one_penalty is False):
                    self.player_one_penalty = True
                    self.player_one_penalty_time = pygame.time.get_ticks()
                if (player_two_answer is not correct_answer and self.player_two_choice is not None and
                        self.player_two_penalty is False):
                    self.player_two_penalty = True
                    self.player_two_penalty_time = pygame.time.get_ticks()

                if self.player_one_score == 5 or self.player_two_score == 5:
                    if self.player_one_score > self.player_two_score:
                        print("Player One is Winner")
                        print("Player 1:", self.player_one_score)
                        print("Player 2:", self.player_two_score)
                        exit(0)
                    else:
                        print("Player Two is Winner")
                        print("Player 1:", self.player_one_score)
                        print("Player 2:", self.player_two_score)
                        exit(0)

            self.player_one_choice = None
            self.player_two_choice = None

    ply_draw_btn = PlayerScore(game_screen_sizes)

    play = True
    while play:
        user_hot_keys_press = False
        back_ground_image_game_play(game_play_bg, game_screen_sizes)
        pygame.draw.rect(game_screen_sizes, (255, 255, 255), ((computer_width_res * 0.20), (computer_height_res * 0.04),
                                                              (computer_width_res * 0.60),
                                                              (computer_height_res * 0.20)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                user_hot_keys_press = True

        ply_draw_btn.validate_answer(user_hot_keys_press)
        pygame.display.update()
