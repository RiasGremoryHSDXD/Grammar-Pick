import os
import random
import QuestionAndAnswer
import pygame
from pygame import mixer

import Button

pygame.init()


def load_animation_frames(base_path, prefix, count):
    return [pygame.image.load(os.path.join(base_path, f"{prefix}{i}.png")) for i in range(1, count + 1)]


# Directory paths
base_dir = "./../ImageStored"
btn_dirs = ["btn_Q", "btn_W", "btn_E", "btn_R", "btn_1", "btn_2", "btn_3", "btn_4"]
btn_prefixes = ["btn_Q", "btn_W", "btn_E", "btn_R", "btn_1", "btn_2", "btn_3", "btn_4"]

# Number of frames for each animation
frame_count = 6

# Load animations
Q_animation, W_animation, E_animation, R_animation, One_animation, Two_animation, Three_animation, Four_animation = [
    load_animation_frames(os.path.join(base_dir, btn_dir), prefix, frame_count) for btn_dir, prefix in zip(btn_dirs,
                                                                                                           btn_prefixes)
]


def play_stage(screen, width_screen, height_screen):
    # Helper function to load and scale images
    def load_scaled_image(path, size):
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)

    # Play Stage BG
    play_stage_bg = load_scaled_image("./../ImageStored/PlayStageBG.png", (width_screen, height_screen))

    # Function to load animation frames
    def load_animation_frame(base_path, count, size):
        frames = []
        for i in range(1, count + 1):
            frame = load_scaled_image(os.path.join(base_path, f"{i}.png"), size)
            frames.append(frame)
        return frames

    # Load animations
    portal = load_animation_frame("./../ImageStored/Portal", 3, (100, 150))
    ply_one_idle = load_animation_frame("./../ImageStored/WizardIdle", 6, (100, 150))
    ply_two_idle = load_animation_frame("./../ImageStored/LadyIdle", 6, (100, 150))
    wiz_att = load_animation_frame("./../ImageStored/WizardAttackMotion", 9, (100, 150))
    fire_ball = load_animation_frame("./../ImageStored/WizardFireBall", 6, (150, 150))
    lady_att = load_animation_frame("./../ImageStored/LadyAttackMotion", 7, (100, 150))
    thunder_bolt_load = load_animation_frame("./../ImageStored/LadyThunderboltBall", 6, (100, 100))
    lady_last_attack = load_animation_frame("./../ImageStored/LadyLastAttack", 11,
                                            (100, height_screen * 0.6))
    wizard_last_attack = load_animation_frame("./../ImageStored/WizardLastAttack", 8, (150, 150))
    wizard_dead = load_animation_frame("./../ImageStored/WizardLost", 6, (100, 150))
    lady_dead = load_animation_frame("./../ImageStored/LadyLost", 5, (100, 150))

    start_fight = load_animation_frame("./../ImageStored/StartFight", 3, (200, 200))

    fight_image = load_scaled_image("./../ImageStored/StartFight/4.png", (width_screen * 0.3, 300))
    start_fight_rect = fight_image.get_rect(center=((width_screen + 200) / 2, (height_screen / 2) * 0.8))

    player_one_won = pygame.image.load("./../ImageStored/Player_1_won.png")
    player_two_won = pygame.image.load("./../ImageStored/Player_2_won.png")

    play_again_btn_img = pygame.image.load("./../ImageStored/play_again.png")
    exit_game_btn_img = pygame.image.load("./../ImageStored/exit_game_btn.png")

    # Sound Effects
    count_fight_se = mixer.Sound("./../MusicStored/321_fight.mp3")
    animation_sound_effect = mixer.Sound("./../MusicStored/PlyWrongPick.mp3")

    # Question and Answer
    grade_1_question_player = QuestionAndAnswer.grade_1_question
    grade_1_choice_answer = QuestionAndAnswer.grade_1_choice

    # Font Text
    font_path = os.path.join('./../FontText/TextFont.ttf')

    fire_sound_effect = mixer.Sound("./../MusicStored/Fire_SE.mp3")
    bolt_sound_effect = mixer.Sound("./../MusicStored/Bolt_SE.mp3")
    click_sound_effect = mixer.Sound("./../MusicStored/Click.mp3")

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

    play_again_btn = Button.ButtonWinner(410, 460, play_again_btn_img, 0.4)
    exit_game_btn = Button.ButtonWinner(730, 460, exit_game_btn_img, 0.4)

    class PlayStage:
        def __init__(self, class_game_screen_sizes, play_width_screen, play_height_screen,
                     class_grade_1_question_player, class_grade_1_choice_answer, class_question_random):
            self.final_att_start_time = None
            self.wiz_final_att_start_time = None
            self.screen_draw = class_game_screen_sizes
            self.scr_wid = play_width_screen
            self.scr_hei = play_height_screen
            self.portal_ani = 0
            self.stepIndex = 0
            self.str_fig_ani = 0
            self.last_update = pygame.time.get_ticks()
            self.last_update_portal = pygame.time.get_ticks()
            self.portal_ani_last = pygame.time.get_ticks()
            self.character_fight_last = pygame.time.get_ticks()
            self.character_fight_last_one = None
            self.character_fight_last_two = None
            self.str_fig_ani_last = None
            self.fight_img = True
            self.wiz_correct = False
            self.char_att_index = 0
            self.wiz_done_ani = None
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
            self.wiz_got_correct = False
            self.lady_got_correct = False
            self.wizard_att_ind = 0
            self.fire_ball_index = 0
            self.fire_ball_time = None
            self.fireball_x = 0
            self.wiz_land_att = False
            self.wiz_start_fire = False
            self.lady_start_fire = False
            self.fire_balls = []
            self.thunder_bolts = []
            # Health
            self.wiz_box = (self.scr_wid * 0.03, self.scr_hei * 0.4, 100, 150)
            self.lady_box = (self.scr_wid * 0.90, self.scr_hei * 0.4, 100, 150)
            self.wiz_health = 100
            self.lady_health = 100
            self.lady_final_att_bool = False
            self.wizard_final_att_bool = False
            self.stepLightIndex = 0
            self.stepMeteoriteIndex = 0
            self.done_final_att = False
            self.wiz_done_final_att = False
            self.stopIndexLig = False
            self.stopIndexMet = False
            self.wizard_dead = False
            self.lady_dead = False
            self.wizard_dead_time = None
            self.lady_dead_time = None
            self.wizard_dead_index = 0
            self.lady_dead_index = 0
            self.lady_done_dead = False
            self.wizard_done_dead = False
            self.bot_met = None

        def portal(self):
            current_time = pygame.time.get_ticks()

            if current_time - self.portal_ani_last >= 5000:
                if self.str_fig_ani_last is None:
                    count_fight_se.play()
                    self.str_fig_ani_last = current_time

                if self.fight_img:
                    self.character_fight()
                elif self.fight_img is False:
                    self.char_att_ani()

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

        def char_att_ani(self):
            current_time = pygame.time.get_ticks()

            if self.wiz_got_correct:
                self.wiz_health_bar()
                self.lady_health_bar()

                if self.stepIndex >= 5:
                    self.stepIndex = 0

                if current_time - self.character_fight_last >= 10:
                    self.character_fight_last = current_time
                    self.stepIndex += 1

                if self.wizard_att_ind == 8:
                    self.wiz_got_correct = False
                    self.wiz_start_fire = True
                    fire_sound_effect.play()
                    self.wizard_att_ind = 0
                else:
                    self.wizard_attack_ani()

                self.screen_draw.blit(wiz_att[self.wizard_att_ind], (self.scr_wid * 0.02, self.scr_hei * 0.4))
                self.screen_draw.blit(ply_two_idle[self.stepIndex], (self.scr_wid * 0.90, self.scr_hei * 0.4))

            elif self.lady_got_correct:
                self.wiz_health_bar()
                self.lady_health_bar()

                if self.stepIndex >= 5:
                    self.stepIndex = 0

                if current_time - self.character_fight_last >= 10:
                    self.character_fight_last = current_time
                    self.stepIndex += 1

                if self.char_att_index == 6:
                    self.lady_got_correct = False
                    self.lady_start_fire = True
                    bolt_sound_effect.play()
                    self.char_att_index = 0
                else:
                    self.lady_attack_ani()

                self.screen_draw.blit(ply_one_idle[self.stepIndex], (self.scr_wid * 0.02, self.scr_hei * 0.4))
                self.screen_draw.blit(lady_att[self.char_att_index], (self.scr_wid * 0.90, self.scr_hei * 0.4))

            else:
                self.wiz_health_bar()
                self.lady_health_bar()

                if self.stepIndex >= 5:
                    self.stepIndex = 0

                if current_time - self.last_update >= 10:
                    self.last_update = current_time
                    self.stepIndex += 1

                self.screen_draw.blit(ply_one_idle[self.stepIndex], (self.scr_wid * 0.02, self.scr_hei * 0.4))
                self.screen_draw.blit(ply_two_idle[self.stepIndex], (self.scr_wid * 0.90, self.scr_hei * 0.4))

        def dead_character_ani(self):

            if self.wizard_dead:
                current_time = pygame.time.get_ticks()

                if self.stepIndex >= 5:
                    self.stepIndex = 0

                if self.wizard_dead_index == 5:
                    self.wizard_done_dead = True

                if current_time - self.wizard_dead_time >= 50 and not self.wizard_done_dead:
                    self.wizard_dead_time = current_time
                    self.wizard_dead_index += 1
                    self.stepIndex += 1

                self.screen_draw.blit(wizard_dead[self.wizard_dead_index], (self.scr_wid * 0.02, self.scr_hei * 0.4))
                self.screen_draw.blit(ply_two_idle[self.stepIndex], (self.scr_wid * 0.90, self.scr_hei * 0.4))

            if self.lady_dead:
                current_time = pygame.time.get_ticks()

                if self.stepIndex >= 5:
                    self.stepIndex = 0

                if self.lady_dead_index == 4:
                    self.lady_done_dead = True

                if current_time - self.lady_dead_time >= 50 and not self.lady_done_dead:
                    self.lady_dead_time = current_time
                    self.stepIndex += 1
                    self.lady_dead_index += 1

                self.screen_draw.blit(ply_one_idle[self.stepIndex], (self.scr_wid * 0.02, self.scr_hei * 0.4))
                self.screen_draw.blit(lady_dead[self.lady_dead_index], (self.scr_wid * 0.90, self.scr_hei * 0.4))

        def shoot(self):
            if self.wiz_start_fire and not self.wiz_got_correct:
                fire_ball_anis = AttackFiredAni(self.screen_draw, self.scr_wid, self.scr_hei * 0.4)
                self.fire_balls.append(fire_ball_anis)
                self.wiz_start_fire = False

        def lady_shoot(self):
            if self.lady_start_fire and not self.lady_got_correct:
                thunder_bolt_anis = AttackThunderAni(self.screen_draw, self.scr_wid, self.scr_hei * 0.4)
                self.thunder_bolts.append(thunder_bolt_anis)
                self.lady_start_fire = False

        def wiz_health_bar(self):
            pygame.draw.rect(self.screen_draw, (255, 0, 0), (self.scr_wid * 0.02, self.scr_hei * 0.4 - 20,
                                                             100, 10))
            pygame.draw.rect(self.screen_draw, (0, 255, 0), (self.scr_wid * 0.02, self.scr_hei * 0.4 - 20,
                                                             self.wiz_health, 10))
            if self.player_two_score == 10 and not self.lady_final_att_bool:
                self.lady_final_att_bool = True
                self.final_att_start_time = pygame.time.get_ticks()

        def lady_health_bar(self):
            pygame.draw.rect(self.screen_draw, (255, 0, 0), (self.scr_wid * 0.9, self.scr_hei * 0.4 - 20,
                                                             100, 10))
            pygame.draw.rect(self.screen_draw, (0, 255, 0), (self.scr_wid * 0.9, self.scr_hei * 0.4 - 20,
                                                             self.lady_health, 10))
            if self.player_one_score == 10 and not self.wizard_final_att_bool:
                self.wizard_final_att_bool = True
                self.wiz_final_att_start_time = pygame.time.get_ticks()

        def wizard_final_att(self, x):
            self.bot_met = pygame.Rect(x, self.scr_hei * 0.35, 150, 150)
            if self.wizard_final_att_bool:
                current_time = pygame.time.get_ticks()

                if self.stepMeteoriteIndex >= 7:
                    self.stepMeteoriteIndex = 0

                if current_time - self.wiz_final_att_start_time >= 100:
                    self.wiz_final_att_start_time = current_time
                    self.stepMeteoriteIndex += 1

                if not self.wiz_done_final_att:
                    self.bot_met.topleft = (x + 10, (self.scr_hei * 0.35) + 10)
                    self.screen_draw.blit(wizard_last_attack[self.stepMeteoriteIndex], (x, self.scr_hei * 0.35))

        def lady_final_att(self):
            if self.lady_final_att_bool:
                current_time = pygame.time.get_ticks()

                if self.stepLightIndex >= 10 and not self.done_final_att:
                    self.stepLightIndex = 0
                    self.lady_final_att_bool = False
                    self.done_final_att = True
                    self.stopIndexLig = True

                if current_time - self.final_att_start_time >= 200 and not self.stopIndexLig:
                    self.final_att_start_time = current_time
                    self.stepLightIndex += 1

                self.screen_draw.blit(lady_last_attack[self.stepLightIndex], (self.scr_wid * 0.02, 0))

        def wizard_attack_ani(self):

            current_time = pygame.time.get_ticks()
            if current_time - self.character_fight_last_one >= 100:
                self.wizard_att_ind = 1
            if current_time - self.character_fight_last_one >= 200:
                self.wizard_att_ind = 2
            if current_time - self.character_fight_last_one >= 300:
                self.wizard_att_ind = 3
            if current_time - self.character_fight_last_one >= 400:
                self.wizard_att_ind = 4
            if current_time - self.character_fight_last_one >= 500:
                self.wizard_att_ind = 5
            if current_time - self.character_fight_last_one >= 600:
                self.wizard_att_ind = 6
            if current_time - self.character_fight_last_one >= 700:
                self.wizard_att_ind = 7
            if current_time - self.character_fight_last_one >= 800:
                self.wizard_att_ind = 8

        def lady_attack_ani(self):

            current_time = pygame.time.get_ticks()
            if current_time - self.character_fight_last_two >= 100:
                self.char_att_index = 1
            if current_time - self.character_fight_last_two >= 250:
                self.char_att_index = 2
            if current_time - self.character_fight_last_two >= 500:
                self.char_att_index = 3
            if current_time - self.character_fight_last_two >= 600:
                self.char_att_index = 4
            if current_time - self.character_fight_last_two >= 700:
                self.char_att_index = 5
            if current_time - self.character_fight_last_two >= 800:
                self.char_att_index = 6

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
                    self.wiz_got_correct = True
                    self.character_fight_last_one = pygame.time.get_ticks()
                    self.player_one_score += 1
                    self.total_score += 1

                if player_two_answer == correct_answer and self.player_two_penalty is False:
                    self.player_one_penalty = False
                    self.player_two_penalty = False
                    self.player_one_animation_count = 0
                    self.player_two_animation_count = 0
                    self.lady_got_correct = True
                    self.character_fight_last_two = pygame.time.get_ticks()
                    self.player_two_score += 1
                    self.total_score += 1

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

            if self.lady_health == 0 or self.wiz_health < 0:
                if self.wiz_health > 0:
                    self.wizard_dead_time = pygame.time.get_ticks()
                    self.lady_dead_time = pygame.time.get_ticks()
                    self.lady_dead = True
                else:
                    self.wizard_dead_time = pygame.time.get_ticks()
                    self.lady_dead_time = pygame.time.get_ticks()
                    self.wizard_dead = True

            self.player_one_choice = None
            self.player_two_choice = None

        def player_winner(self):
            ply_win_img = None

            if self.wizard_dead:
                ply_win_img = player_two_won
            if self.lady_dead:
                ply_win_img = player_one_won

            ply_img_sz = pygame.transform.scale(ply_win_img, (400, 400))
            ply_img_sz_rect = ply_win_img.get_rect(center=((self.scr_wid - 115) / 2, (self.scr_hei - 150) / 2))

            self.screen_draw.blit(ply_img_sz, ply_img_sz_rect)
            self.ply_after_win_btn()

        def ply_after_win_btn(self):
            if play_again_btn.after_win_btn(self.screen_draw)[0]:
                click_sound_effect.play()
                return play_stage(self.screen_draw, self.scr_wid, self.scr_hei)
            if exit_game_btn.after_win_btn(self.screen_draw)[0]:
                click_sound_effect.play()
                exit(0)
            if (play_again_btn.after_win_btn(self.screen_draw)[1] or
                    exit_game_btn.after_win_btn(self.screen_draw)[1]):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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

    class AttackFiredAni:
        def __init__(self, game_screen, x, y):
            self.screen = game_screen
            self.x_loc = (x * 0.02) + 100
            self.y_loc = y
            self.fire_ball = pygame.Rect(self.x_loc + 10, self.y_loc + 20, 100, 100)

            self.fireball_images = [fire_ball[0], fire_ball[1], fire_ball[2], fire_ball[3], fire_ball[4], fire_ball[5]]
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.animation_delay = 300  # Milliseconds between frames

        def draw_wiz_fire(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update > self.animation_delay:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.fireball_images)

            self.fire_ball.topleft = (self.x_loc + 10, self.y_loc + 20)
            self.screen.blit(self.fireball_images[self.current_frame], (self.x_loc, self.y_loc))

        def move(self):
            self.x_loc += 20
            self.fire_ball.x = self.x_loc

    class AttackThunderAni:
        def __init__(self, game_screen, x, y):
            self.screen = game_screen
            self.x_loc = (x * 0.9) - 100
            self.y_loc = y
            self.thunder_bolt = pygame.Rect(self.x_loc, self.y_loc, 100, 100)

            self.thunder_bolt_images = [thunder_bolt_load[0], thunder_bolt_load[1], thunder_bolt_load[2],
                                        thunder_bolt_load[3], thunder_bolt_load[4], thunder_bolt_load[5]]
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.animation_delay = 300  # Milliseconds between frames

        def draw_lady_thunder_bolt(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update > self.animation_delay:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.thunder_bolt_images)

            self.thunder_bolt.topleft = (self.x_loc + 10, self.y_loc + 20)
            self.screen.blit(self.thunder_bolt_images[self.current_frame], (self.x_loc, self.y_loc))

        def move(self):
            self.x_loc -= 20
            self.thunder_bolt.x = self.x_loc

    rect_x = width_screen * 0.20
    rect_y = height_screen * 0.04
    rect_width = width_screen * 0.60
    rect_height = height_screen * 0.20
    pop_question_loc = list(range(len(grade_1_question_player)))
    question_random = []
    wiz_final_att_x = (width_screen * 0.02) + 100
    while True:
        random_question = random.randint(0, len(pop_question_loc) - 1)
        question_pop = pop_question_loc.pop(random_question)
        question_random.append(question_pop)

        if not pop_question_loc:
            break

    ply_draw_btn = PlayStage(screen, width_screen, height_screen, grade_1_question_player, grade_1_choice_answer,
                             question_random)

    time = pygame.time.get_ticks()

    # In the main game loop
    while True:
        pygame.display.set_caption("Game Play")

        current_count = pygame.time.get_ticks()
        user_hot_keys_press = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                user_hot_keys_press = True

        screen.blit(play_stage_sz, (0, 0))
        ply_draw_btn.portal()

        if current_count - time >= 9000:
            screen.blit(play_stage_sz, (0, 0))
            ply_draw_btn.shoot()
            ply_draw_btn.lady_shoot()

            if not ply_draw_btn.lady_dead and not ply_draw_btn.wizard_dead:
                ply_draw_btn.char_att_ani()
                ply_draw_btn.validate_answer(user_hot_keys_press)
            else:
                ply_draw_btn.dead_character_ani()
                ply_draw_btn.player_winner()

        for fire_ball_ani in ply_draw_btn.fire_balls:
            if not ply_draw_btn.wizard_final_att_bool:
                fire_ball_ani.move()
                fire_ball_ani.draw_wiz_fire()

                lady_hit_box = pygame.Rect(ply_draw_btn.scr_wid * 0.90, ply_draw_btn.scr_hei * 0.4, 100, 150)
                if fire_ball_ani.fire_ball.colliderect(lady_hit_box):
                    ply_draw_btn.lady_health -= 10
                    ply_draw_btn.fire_balls.remove(fire_ball_ani)
            else:
                wiz_final_att_x += 20
                ply_draw_btn.wizard_final_att(wiz_final_att_x)

                lady_hit_box = pygame.Rect(ply_draw_btn.scr_wid * 0.90, ply_draw_btn.scr_hei * 0.4, 100, 150)
                if ply_draw_btn.bot_met.colliderect(lady_hit_box) and not ply_draw_btn.wiz_done_final_att:
                    ply_draw_btn.lady_health -= 10
                    ply_draw_btn.wiz_done_final_att = True

        for thunder_bolt in ply_draw_btn.thunder_bolts:
            if not ply_draw_btn.lady_final_att_bool:
                thunder_bolt.move()
                thunder_bolt.draw_lady_thunder_bolt()

                wizard_hit_box = pygame.Rect(ply_draw_btn.scr_wid * 0.02, ply_draw_btn.scr_hei * 0.4, 100, 150)
                if thunder_bolt.thunder_bolt.colliderect(wizard_hit_box):
                    ply_draw_btn.wiz_health -= 10
                    ply_draw_btn.thunder_bolts.remove(thunder_bolt)
            else:
                ply_draw_btn.lady_final_att()
                ply_draw_btn.wiz_health -= 10

        pygame.display.update()
