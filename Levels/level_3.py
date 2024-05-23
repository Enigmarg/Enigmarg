import json
import pygame
from Classes.question_pool import QuestionPool
from Levels.level import Level
from Levels.level_4 import Level4
from UI.button import Button
from UI.score import Score
from util import WINDOW_SIZE, break_line

# TELA DE JOGO

class Level3(Level):
    def __init__(self, screen, transition_call):
        super().__init__(screen, transition_call)
        # Fetch data from database
        with open("./resources/questions.json", "r", -1, "UTF-8") as file:
            data = json.load(file)
            self.pool = QuestionPool(data)

        self.screen = screen
        self.images = {}
        self.texts = []
        self.answer_btn = []
        self.pos = 0
        self.voltar = Button((10, 465), (150, 50), pygame.Color("gray"), "Voltar")
        self.text = self.pool.get_question()
        self.answers:list[dict] = self.pool.get_answers()
        self.score = Score((10, 10), (100, 50), pygame.Color("gray"))
        self.len_questions = len(self.pool.questions)

    def load(self):
        self.images = {
            "background": pygame.image.load("./resources/background.png")
                                                    .convert_alpha(),
            "chalkboard": pygame.transform.scale_by(pygame.image.load("./resources/chalkboard.png")
                                                    .convert_alpha(), 1.5)
        }

        self.next_question(True)

        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.images["background"], (self.pos - WINDOW_SIZE[0], 0))

        self.pos += 1

        if self.pos >= WINDOW_SIZE[0]:
            self.pos = 0

        self.screen.blit(self.images["chalkboard"], (WINDOW_SIZE[0] / 2 - 150 * 1.5, 20))
        for i in self.texts:
            i.draw(self.screen)

        # Não mexer, não sei oq faz mas funciona
        cur_level = str.format(f'Level {self.len_questions
                                         - len(self.pool.questions) + 1} / {self.len_questions}')
        font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)
        text = font.render(cur_level, True, pygame.Color("gray"))

        self.screen.blit(text, (WINDOW_SIZE[0] / 2 - text.get_width() / 2, 35))

        self.score.draw(self.screen)

        for answer_btn in self.answer_btn:
            answer_btn.draw(self.screen)
            if answer_btn.check_button():
                if self.pool.is_correct_answer(answer_btn.text):
                    self.next_question()
                else:
                    self.next_question()

    def next_question(self, first=False):
        self.score.increment_score()
        if len(self.pool.questions) == 1:
            self.transition_call(Level4(self.screen, self.transition_call, self.score.score))
        else:
            if not first:
                self.pool.questions.pop(0)
                self.pool.next_question()
            self.text = self.pool.get_question()
            self.answers = self.pool.get_answers()
            self.answer_btn = []
            for a in self.answers:
                self.answer_btn.append(Button((WINDOW_SIZE[0] / 2 - 150,
                                                WINDOW_SIZE[1] / 2 + 120 *
                                                  self.answers.index(a) / 2 + 50)
                                              , (300, 40), pygame.Color("gray"), a["text"]))
            self.texts = break_line(self.text,
                                     pygame.Vector2(WINDOW_SIZE[0] / 2 - 150 * 1.5 + 30, 40))
