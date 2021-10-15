class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        keep_running = True

        while keep_running:
            for question in self.question_list:
                answer = input(f"Q.{self.question_number + 1}: {question.text} "
                               f"(True/False)? ").title()
                self.question_number += 1
                if answer == question.answer or answer == question.answer[0]:
                    print("You got it right!")
                    self.score += 1
                else:
                    print("That's wrong.")
                if self.question_number != len(self.question_list):
                    print(f"The correct answer was: {question.answer}.")
                    print(f"Your current score is: {self.score}/{self.question_number}\n")
                else:
                    print("\nYou've completed the quiz.")
                    print(f"Your final score was: {self.score}/{self.question_number}")
            keep_running = False
