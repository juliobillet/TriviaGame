from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dictionary in question_data:
    question_bank.append(Question(dictionary['question'], dictionary['correct_answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()
