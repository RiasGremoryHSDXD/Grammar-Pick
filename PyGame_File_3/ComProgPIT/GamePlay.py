import pygame
import os.path
import Button
import QuestionAndAnswer
import random
from pygame import mixer

pygame.init()

# Background Image
position = (0, 0)
game_play_bg = pygame.image.load("./../GameImageStored/GamePlayBG.png")
score_count_bg = pygame.image.load("./../GameImageStored/score_count.png")
player_one_winner = pygame.image.load("./../GameImageStored/player_one_win.png")
player_two_winner = pygame.image.load("./../GameImageStored/player_two_win.png")

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

grade_1_question_player = QuestionAndAnswer.grade_1_question
grade_1_choice_answer = QuestionAndAnswer.grade_1_choice

animation_sound_effect = mixer.Sound("./../GameMusicStored/PlyWrongPick.mp3")
correct_answer_sound_effect = mixer.Sound("./../GameMusicStored/PlyCorrectPick.mp3")


def user_play(game_screen_sizes, computer_width_res, computer_height_res):
    pygame.display.set_caption("Game Stage")
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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

        def __init__(self, class_game_screen_sizes, class_grade_1_question_player, class_grade_1_choice_answer,
                     class_question_random):
            self.player_one_score = 0
            self.player_two_score = 0
            self.player_one_choice = None
            self.player_two_choice = None
            self.player_one_arr_ans = ["Q", "W", "E", "R"]
            self.player_two_arr_ans = [1, 2, 3, 4]
            self.player_one_penalty = False
            self.player_two_penalty = False
            self.player_penalty_time = 0
            self.player_one_penalty_time = None
            self.player_two_penalty_time = None
            self.player_one_animation_count = 0
            self.player_two_animation_count = 0
            self.class_game_screen_size = class_game_screen_sizes
            self.class_grade_1_question_player = class_grade_1_question_player
            self.class_grade_1_choice_answer = class_grade_1_choice_answer
            self.total_score = 0
            self.class_question_random = class_question_random
            self.player_one_is_winner = False
            self.player_two_is_winner = False
            self.have_winner = False
            self.end_game = None

        def player_one_button(self):
            screen_size = self.class_game_screen_size
            ply_one_ani = self.player_one_animation_count
            q_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][0]
            w_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][1]
            e_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][2]
            r_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][3]
            penalty = self.player_one_penalty, self.have_winner

            if (ply_one_first_choice.player_one_btn_draw(screen_size, Q_animation, ply_one_ani, q_choice, penalty)
                    == "Q"):
                self.player_one_choice = ply_one_first_choice.player_one_btn_draw(screen_size, Q_animation,
                                                                                  ply_one_ani, q_choice,
                                                                                  penalty)
            if (ply_one_second_choice.player_one_btn_draw(screen_size, W_animation, ply_one_ani, w_choice, penalty)
                    == "W"):
                self.player_one_choice = ply_one_second_choice.player_one_btn_draw(screen_size, W_animation,
                                                                                   ply_one_ani, w_choice,
                                                                                   penalty)
            if (ply_one_third_choice.player_one_btn_draw(screen_size, E_animation, ply_one_ani, e_choice, penalty)
                    == "E"):
                self.player_one_choice = ply_one_third_choice.player_one_btn_draw(screen_size, E_animation,
                                                                                  ply_one_ani, e_choice,
                                                                                  penalty)
            if (ply_one_fourth_choice.player_one_btn_draw(screen_size, R_animation, ply_one_ani, r_choice, penalty)
                    == "R"):
                self.player_one_choice = ply_one_fourth_choice.player_one_btn_draw(screen_size, R_animation,
                                                                                   ply_one_ani, r_choice,
                                                                                   penalty)

            if self.player_one_choice is not None and self.player_one_choice in self.player_one_arr_ans:
                player_one_convert = self.player_one_arr_ans.index(self.player_one_choice)
                self.player_one_choice = [q_choice, w_choice, e_choice, r_choice]
                self.player_one_choice = self.player_one_choice[player_one_convert]
                return self.player_one_choice

            return self.player_two_choice

        def player_two_button(self):
            screen_size = self.class_game_screen_size
            ply_two_ani = self.player_two_animation_count
            one_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][0]
            two_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][1]
            three_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][2]
            four_choice = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][3]
            penalty = self.player_two_penalty, self.have_winner

            if (ply_two_first_choice.player_two_btn_draw(screen_size, One_animation, ply_two_ani, one_choice,
                                                         penalty) == 1):
                self.player_two_choice = ply_two_first_choice.player_two_btn_draw(screen_size, One_animation,
                                                                                  ply_two_ani, one_choice, penalty)
            if (ply_two_second_choice.player_two_btn_draw(screen_size, Two_animation, ply_two_ani, two_choice,
                                                          penalty) == 2):
                self.player_two_choice = ply_two_second_choice.player_two_btn_draw(screen_size, Two_animation,
                                                                                   ply_two_ani, two_choice, penalty)
            if (ply_two_third_choice.player_two_btn_draw(screen_size, Three_animation, ply_two_ani, three_choice,
                                                         penalty) == 3):
                self.player_two_choice = ply_two_third_choice.player_two_btn_draw(screen_size, Three_animation,
                                                                                  ply_two_ani, three_choice, penalty)
            if (ply_two_fourth_choice.player_two_btn_draw(screen_size, Four_animation, ply_two_ani, four_choice,
                                                          penalty) == 4):
                self.player_two_choice = ply_two_fourth_choice.player_two_btn_draw(screen_size, Four_animation,
                                                                                   ply_two_ani, four_choice, penalty)

            if self.player_two_choice is not None and self.player_two_choice in self.player_two_arr_ans:
                player_two_convert = self.player_two_arr_ans.index(self.player_two_choice)
                self.player_two_choice = [one_choice, two_choice, three_choice, four_choice]
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

        def force_exit(self):
            if self.player_one_is_winner is True or self.player_two_is_winner is True:
                if pygame.time.get_ticks() - self.end_game >= 5000:
                    exit(0)

        def validate_answer(self, hot_keys_press):
            correct_answer = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][4]
            player_one_answer = ply_draw_btn.player_one_button()
            player_two_answer = ply_draw_btn.player_two_button()
            self.players_time_penalty()
            self.force_exit()
            if self.have_winner is False:
                self.question_answer()
            self.score_board()

            if self.player_one_is_winner is True or self.player_two_is_winner is True:
                self.have_winner = True

            if hot_keys_press:
                if player_one_answer == correct_answer and self.player_one_penalty is False:
                    correct_answer_sound_effect.play()
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.player_two_animation_count = 0
                    self.player_one_score += 1
                    self.total_score += 1
                if player_two_answer == correct_answer and self.player_two_penalty is False:
                    correct_answer_sound_effect.play()
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.total_score += 1
                    self.player_two_animation_count = 0
                    self.player_two_score += 1
                if (player_one_answer is not correct_answer and self.player_one_choice is not None and
                        self.player_one_penalty is False):
                    animation_sound_effect.play()
                    self.player_one_penalty = True
                    self.player_one_penalty_time = pygame.time.get_ticks()
                if (player_two_answer is not correct_answer and self.player_two_choice is not None and
                        self.player_two_penalty is False):
                    animation_sound_effect.play()
                    self.player_two_penalty = True
                    self.player_two_penalty_time = pygame.time.get_ticks()

                if self.player_one_score == 10 or self.player_two_score == 10:
                    if self.player_one_score > self.player_two_score:
                        self.player_one_is_winner = True
                        self.end_game = pygame.time.get_ticks()
                    else:
                        self.player_two_is_winner = True
                        self.end_game = pygame.time.get_ticks()

            if self.player_one_is_winner is True or self.player_two_is_winner is True:
                self.player_winner()

            self.player_one_choice = None
            self.player_two_choice = None

        def question_answer(self):
            question = self.class_grade_1_question_player[self.class_question_random[self.total_score]]
            base_font_size = 30
            max_width = (rect_x + rect_y) * 70
            font = pygame.font.SysFont("gagalin", base_font_size)
            text_width, text_height = font.size(question)

            while text_width > max_width:
                base_font_size -= 5
                font = pygame.font.SysFont("gagalin", base_font_size)
                text_width, text_height = font.size(question)

            text_question = font.render(question, True, (255, 0, 255))
            text_width, text_height = text_question.get_size()
            center_x = rect_x + (rect_width - text_width) / 2
            center_y = rect_y + (rect_height - text_height) / 2
            game_screen_sizes.blit(text_question, (center_x, center_y))

        def score_board(self):
            ply_score_board = f"{self.player_one_score:02d} : {self.player_two_score:02d}"
            score_font = pygame.font.SysFont("gagalin", 50)
            score_board_render = score_font.render(ply_score_board, True, (43, 58, 141))
            ply_score_board_width, ply_score_board_height = score_board_render.get_size()
            score_board_x = score_count_x + (score_count_width - ply_score_board_width) / 2
            score_board_y = score_count_y + (score_count_height - ply_score_board_height) / 2
            game_screen_sizes.blit(score_board_render, (score_board_x, score_board_y))

        def player_winner(self):
            ply_win_img = None
            if self.player_one_is_winner is True:
                ply_win_img = player_one_winner
            if self.player_two_is_winner is True:
                ply_win_img = player_two_winner

            ply_win_img_size = pygame.transform.scale(ply_win_img, (computer_width_res * 0.6,
                                                                    computer_height_res * 0.8))
            ply_win_img_width, ply_win_img_height = ply_win_img_size.get_size()
            ply_win_img_x = (computer_width_res - ply_win_img_width) / 2
            ply_win_img_y = ((computer_height_res - ply_win_img_height) / 2)
            game_screen_sizes.blit(ply_win_img_size, (ply_win_img_x, ply_win_img_y))

    rect_x = computer_width_res * 0.20
    rect_y = computer_height_res * 0.04
    rect_width = computer_width_res * 0.60
    rect_height = computer_height_res * 0.20
    pop_question_loc = list(range(len(grade_1_question_player)))
    question_random = []

    while True:
        random_question = random.randint(0, len(pop_question_loc) - 1)
        question_pop = pop_question_loc.pop(random_question)
        question_random.append(question_pop)

        if not pop_question_loc:
            break

    ply_draw_btn = PlayerScore(game_screen_sizes, grade_1_question_player, grade_1_choice_answer, question_random)

    score_count = pygame.transform.scale(score_count_bg, (computer_width_res * 0.20, computer_height_res * 0.10))
    score_count_width, score_count_height = score_count.get_size()
    score_count_x = (computer_width_res - score_count_width) / 2
    score_count_y = ((computer_height_res - score_count_height) / 2) * 0.80

    play = True
    while play:
        user_hot_keys_press = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                user_hot_keys_press = True

        back_ground_image_game_play(game_play_bg, game_screen_sizes)
        pygame.draw.rect(game_screen_sizes, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))
        game_screen_sizes.blit(score_count, (score_count_x, score_count_y))

        ply_draw_btn.validate_answer(user_hot_keys_press)
        pygame.display.update()
