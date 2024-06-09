import os
import pygame
import QuestionAndAnswer
import Button
import random
from pygame import mixer


pygame.init()

# width_screen = 1200
# height_screen = 700
# screen = pygame.display.set_mode((width_screen, height_screen))

# Play Stage BG
play_stage_bg = pygame.image.load("./../ImageStored/PlayStageBG.png")

# Portal Animation
portal = [None] * 3
for picIndex in range(1, 4):
    image = pygame.image.load(os.path.join("./../ImageStored/Portal/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 150))
    portal[picIndex - 1] = scaled_image

# Character Animation
ply_one_idle = [None] * 6
for picIndex in range(1, 7):
    image = pygame.image.load(os.path.join("./../ImageStored/WizardIdle/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 150))
    ply_one_idle[picIndex - 1] = scaled_image

ply_two_idle = [None] * 6
for picIndex in range(1, 7):
    image = pygame.image.load(os.path.join("./../ImageStored/LadyIdle/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 150))
    ply_two_idle[picIndex - 1] = scaled_image

# Count Fight Animation

# Choice Player Answer Animation
Q_animation = [None] * 6
for picIndex in range(1, 7):
    Q_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_Q/" + "btn_Q" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

W_animation = [None] * 6
for picIndex in range(1, 7):
    W_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_W/" + "btn_W" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

E_animation = [None] * 6
for picIndex in range(1, 7):
    E_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_E/" + "btn_E" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

R_animation = [None] * 6
for picIndex in range(1, 7):
    R_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_R/" + "btn_R" + str(picIndex) +
                                                               ".png"))
    picIndex += 1

One_animation = [None] * 6
for picIndex in range(1, 7):
    One_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_1/" + "btn_1" + str(picIndex)
                                                                 + ".png"))
    picIndex += 1

Two_animation = [None] * 6
for picIndex in range(1, 7):
    Two_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_2/" + "btn_2" + str(picIndex)
                                                                 + ".png"))
    picIndex += 1

Three_animation = [None] * 6
for picIndex in range(1, 7):
    Three_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_3/" + "btn_3" +
                                                                   str(picIndex) + ".png"))
    picIndex += 1

Four_animation = [None] * 6
for picIndex in range(1, 7):
    Four_animation[picIndex - 1] = pygame.image.load(os.path.join("./../ImageStored/btn_4/" + "btn_4" +
                                                                  str(picIndex) + ".png"))
    picIndex += 1

wiz_att = [None] * 9
for picIndex in range(1, 10):
    image = pygame.image.load(os.path.join("./../ImageStored/WizardAttackMotion/" + str(picIndex) + ".png"))
    scaled_image = pygame.transform.scale(image, (100, 150))
    wiz_att[picIndex - 1] = scaled_image

fight_image = pygame.image.load("./../ImageStored/StartFight/4.png")


# Sound Effects
count_fight_se = mixer.Sound("./../MusicStored/321_fight.mp3")
animation_sound_effect = mixer.Sound("./../MusicStored/PlyWrongPick.mp3")


# Question and Answer
grade_1_question_player = QuestionAndAnswer.grade_1_question
grade_1_choice_answer = QuestionAndAnswer.grade_1_choice

# Font Text
font_path = os.path.join('./../FontText/TextFont.ttf')


def play_stage(screen, width_screen, height_screen):

    # Count Fight Animation
    start_fight = [None] * 3
    for picIndex in range(1, 4):
        image = pygame.image.load(os.path.join("./../ImageStored/StartFight/" + str(picIndex) + ".png"))
        scaled_image = pygame.transform.scale(image, (200, 200))
        start_fight_rect = scaled_image.get_rect(center=(width_screen / 2, (height_screen / 2) * 0.8))
        start_fight[picIndex - 1] = scaled_image

    fight_image_sz = pygame.transform.scale(fight_image, (width_screen * 0.3, 300))
    fight_image_sz_rect = fight_image_sz.get_rect(center=(width_screen / 2, (height_screen / 2) * 0.8))

    play_stage_sz = pygame.transform.scale(play_stage_bg, (width_screen, height_screen))
    mixer.music.load("./../MusicStored/play_stage_bg.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    ply_one_first_choice = Button.AnswerButton(10, 60, width_screen, height_screen)
    ply_one_second_choice = Button.AnswerButton(25, 60, width_screen, height_screen)
    ply_one_third_choice = Button.AnswerButton(10, 80, width_screen, height_screen)
    ply_one_fourth_choice = Button.AnswerButton(25, 80, width_screen, height_screen)

    ply_two_first_choice = Button.AnswerButton(65, 60, width_screen, height_screen)
    ply_two_second_choice = Button.AnswerButton(80, 60, width_screen, height_screen)
    ply_two_third_choice = Button.AnswerButton(65, 80, width_screen, height_screen)
    ply_two_fourth_choice = Button.AnswerButton(80, 80, width_screen, height_screen)

    class PlayStage:
        def __init__(self, play_screen, play_width_screen, play_height_screen):
            self.screen_draw = play_screen
            self.scr_wid = play_width_screen
            self.scr_hei = play_height_screen
            self.portal_ani = 0
            self.stepIndex = 0
            self.str_fig_ani = 0
            self.last_update = pygame.time.get_ticks()
            self.last_update_portal = pygame.time.get_ticks()
            self.portal_ani_last = pygame.time.get_ticks()
            self.str_fig_ani_last = None
            self.fight_img = True
            self.wiz_correct = False

        def portal(self):
            current_time = pygame.time.get_ticks()

            if current_time - self.portal_ani_last >= 5000:
                if self.str_fig_ani_last is None:
                    count_fight_se.play()
                    self.str_fig_ani_last = current_time
                self.character_fight()
            else:
                if self.portal_ani >= 4:
                    self.portal_ani = 0

                if current_time - self.last_update_portal >= 50:
                    self.last_update_portal = current_time
                    self.portal_ani += 1

                self.screen_draw.blit(portal[self.portal_ani // 2], (self.scr_wid * 0.90, self.scr_hei * 0.4))
                self.screen_draw.blit(portal[self.portal_ani // 2], (self.scr_wid * 0.02, self.scr_hei * 0.4))

        def character_fight(self):
            current_time = pygame.time.get_ticks()
            self.count_fight()
            if self.stepIndex >= 8:
                self.stepIndex = 0

            if current_time - self.last_update >= 50:
                self.last_update = current_time
                self.stepIndex += 1

            self.screen_draw.blit(ply_one_idle[self.stepIndex // 2], (self.scr_wid * 0.02, self.scr_hei * 0.4))
            self.screen_draw.blit(ply_two_idle[self.stepIndex // 2], (self.scr_wid * 0.90, self.scr_hei * 0.4))

        def count_fight(self):
            current_time = pygame.time.get_ticks()

            if current_time - self.str_fig_ani_last >= 3000:
                if self.fight_img:
                    self.screen_draw.blit(fight_image_sz, fight_image_sz_rect)
                if current_time - self.str_fig_ani_last >= 4000:
                    self.fight_img = False

            else:
                if current_time - self.str_fig_ani_last >= 2000:
                    self.str_fig_ani = 2

                elif current_time - self.str_fig_ani_last >= 1000:
                    self.str_fig_ani = 1

                elif current_time - self.str_fig_ani_last >= 10:
                    self.str_fig_ani = 0

                self.screen_draw.blit(start_fight[self.str_fig_ani], start_fight_rect)

        def done_fight_ani(self):
            if self.fight_img is False:
                return True

    class PlayScore:
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
                                                                                  ply_two_ani, three_choice,
                                                                                  penalty)
            if (ply_two_fourth_choice.player_two_btn_draw(screen_size, Four_animation, ply_two_ani, four_choice,
                                                          penalty) == 4):
                self.player_two_choice = ply_two_fourth_choice.player_two_btn_draw(screen_size, Four_animation,
                                                                                   ply_two_ani, four_choice,
                                                                                   penalty)

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

        def validate_answer(self, hot_keys_press):
            correct_answer = self.class_grade_1_choice_answer[self.class_question_random[self.total_score]][4]
            player_one_answer = ply_draw_btn.player_one_button()
            player_two_answer = ply_draw_btn.player_two_button()
            self.players_time_penalty()
            if self.have_winner is False:
                self.question_answer()

            if self.player_one_is_winner is True or self.player_two_is_winner is True:
                self.have_winner = True

            if hot_keys_press:
                if player_one_answer == correct_answer and self.player_one_penalty is False:
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.player_two_animation_count = 0
                    self.player_one_score += 1
                    self.total_score += 1
                if player_two_answer == correct_answer and self.player_two_penalty is False:
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
                # self.player_winner()
                print("Player Winner")
            self.player_one_choice = None
            self.player_two_choice = None

        def question_answer(self):
            question = self.class_grade_1_question_player[self.class_question_random[self.total_score]]
            base_font_size = 50
            max_width = width_screen * 0.8
            font = pygame.font.Font(font_path, base_font_size)
            text_width, text_height = font.size(question)

            while text_width > max_width and base_font_size > 0:
                base_font_size -= 1
                font = pygame.font.Font(font_path, base_font_size)
                text_width, text_height = font.size(question)

            text_question = font.render(question, True, 'yellow')
            text_width, text_height = text_question.get_size()
            center_x = rect_x + (rect_width - text_width) / 2
            center_y = rect_y + (rect_height - text_height) / 2
            screen.blit(text_question, (center_x, center_y - 40))

    rect_x = width_screen * 0.20
    rect_y = height_screen * 0.04
    rect_width = width_screen * 0.60
    rect_height = height_screen * 0.20
    pop_question_loc = list(range(len(grade_1_question_player)))
    question_random = []

    while True:
        random_question = random.randint(0, len(pop_question_loc) - 1)
        question_pop = pop_question_loc.pop(random_question)
        question_random.append(question_pop)

        if not pop_question_loc:
            break

    portal_animation = PlayStage(screen, width_screen, height_screen)
    ply_draw_btn = PlayScore(screen, grade_1_question_player, grade_1_choice_answer, question_random)

    while True:
        user_hot_keys_press = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                user_hot_keys_press = True

        screen.blit(play_stage_sz, (0, 0))
        portal_animation.portal()

        if portal_animation.done_fight_ani():
            ply_draw_btn.validate_answer(user_hot_keys_press)
        pygame.display.update()
