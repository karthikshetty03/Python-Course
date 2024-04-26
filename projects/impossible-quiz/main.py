import time
from dataclasses import dataclass
from random import choice, shuffle


@dataclass(slots=True)
class Question:
    question: str
    answers: list[str]
    correct: str


def random_question(question_list: list[Question]) -> int:
    question = choice(question_list)
    print(question.question)
    shuffle(question.answers)
    for i, answer in enumerate(question.answers):
        print(f"{i + 1}. {answer}")

    user_input: str = input("\nEnter your answer >> ").lower().strip()

    if user_input == question.correct:
        print("Correct!")
        question_list.remove(question)
        return 1
    else:
        print(f"Wrong answer:, the correct answer is {question.correct.capitalize()}")
        question_list.remove(question)
        return 0


def run_quiz(questions_box: list[Question]):
    total_score: int = 0
    while questions_box:
        score: int = random_question(question_list=questions_box)
        total_score += score
        time.sleep(2)
    else:
        print(f"Game over! Your score is {total_score}")


def get_questions() -> list[Question]:
    # Questions related to India
    return [
        Question("What is the capital of India?",
                 ["Mumbai", "Delhi", "Bangalore", "Chennai"],
                 "delhi"),
        Question("Which is the national animal of India?",
                 ["Tiger", "Lion", "Elephant", "Leopard"],
                 "tiger"),
        Question("Which is the national bird of India?",
                 ["Peacock", "Sparrow', 'Pigeon", "Parrot"],
                 "peacock"),
        Question("Which is the national flower of India?",
                 ["Rose", "Lotus", "Lily", "Sunflower"],
                 "lotus"),
        Question("Which is the national tree of India?",
                 ["Banyan", "Neem", "Peepal", "Mango"],
                 "banyan"),
        Question("Which is the national fruit of India?",
                 ["Mango", "Banana", "Apple", "Orange"],
                 "mango"),
        Question("Which is the national river of India?",
                 ["Ganga", "Yamuna", "Godavari", "Krishna"],
                 "ganga"),
        Question("Which is the national game of India?",
                 ["Cricket", "Hockey", "Football", "Tennis"],
                 "hockey"),
        Question("Which is the national song of India?",
                 ["Vande Mataram", "Jana Gana Mana", "Saare Jahan Se Achha", "Sare Jahan Se Achha"],
                 "vande mataram"),
        Question("Which is the national anthem of India?",
                 ["Vande Mataram", "Jana Gana Mana", "Saare Jahan Se Achha", "Sare Jahan Se Achha"],
                 "jana gana mana")
    ]


if __name__ == '__main__':
    questions: list[Question] = get_questions()
    run_quiz(questions_box=questions)
