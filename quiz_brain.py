class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.check_answer()
        return f"             Question {self.question_number}:\n\n{self.current_question.text}"


    def check_answer(self):
        correct_answer = self.current_question.answer
        return bool(correct_answer)

