from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    question_bank.append(Question(question_text, question_ans))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() == True:
    quiz.next_question()
