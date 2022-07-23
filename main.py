


#quiz

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 10
QUESTIONS = {
    "How many bones are in the human body": [
        "206", "211", "185", "234"
    ],
    "Which is the main gas that makes up the Earth's atmosphere": [
         "Nitrogen", "Oxygen", "Helium", "Carbon Dioxide"
    ],
    "At what temperature are Celsius and Fahrenheit equal": [
        "-40", "40", "-30", "-45"
    ],
    "What modern-day country was Marie Curie born in": [
        "Poland", "Italy", "France", "Germany"
    ],
    "What was the name of the first man-made satellite launched by the Soviet Union in 1957?": [
        "Sputnik 1", "Sputnik 2", "Kondor", "Kazakh"
    ],
    "What is the biggest planet in our solar system?": [
        "Jupiter", "Uranus", "Venus", "Earth"
    ],
    "How many colors are in the rainbow?": [
        "Seven", "Nine", "Six", "Ten"
    ],
    "What is the hardest natural substance on Earth?": [
        "Diamond", "Titanium", "Gold", "Kevlar"
    ],
    "Does sound travel faster in the air or in water?": [
        "Water", "Air"
    ],
    "What is the largest desert in the world?" : [
        "Antarctica", "Sahara", "Arctic", "Australian"
    ]
}

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1    #True
    else:
        print(f"The answer is {correct_answer!r}, not {answer}")
        return 0    #False

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"You got {num_correct} correct out of {num} questions")

if __name__ == "__main__":
    run_quiz()