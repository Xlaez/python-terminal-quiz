from control import question_bank
class Logic:
    def __init__(self, question_list) -> None:
        self.quiz_number = 0
        self.question_list =question_list
        self.score = 0
    def next_question(self):
        question_next = self.question_list[self.quiz_number].text
        self.quiz_number +=1
        user_answer = input(f"Q.{self.quiz_number}: {question_next} (True/False)").lower()
        print(user_answer)
        correct_answer = self.question_list[self.quiz_number].answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.quiz_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if(user_answer == correct_answer):
            print("You got it right !!!")
            self.score +=1
        else:
            print("That is wrong")
        print(f"The correct answer was :  {correct_answer}.")
        print(f"Your score is : {self.score}/ {self.quiz_number}")
        print("\n")
        # self.still_has_questions = False
new_quiz_logic = Logic(question_bank)
# new_quiz_logic.still_has_questions()

while  new_quiz_logic.still_has_questions():
    new_quiz_logic.next_question()
