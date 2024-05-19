class QuestionPool:
    def __init__(self, questions: list[dict]):
        self.questions = questions
        self.current_question = 0

    def get_question(self) -> str:
        return self.questions[self.current_question]["question"]
    
    def next_question(self) -> None:
        self.current_question += 1
        if self.current_question == len(self.questions):
            self.current_question = 0