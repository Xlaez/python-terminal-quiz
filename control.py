from quiz_model import Question
from quiz_data import data
# from quiz_logic import Logic
question_bank = []


for d in data:
    question_text = d["question"]
    question_answer = d["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


# quiz = Logic(question_bank)
# quiz.next_question()


