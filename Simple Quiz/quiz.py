"""Command line-based quiz game"""


def quiz():

    quiz_questions = [
        ("What is the capital of France?", [
         "Berlin", "Paris", "Madrid", "Rome"], 2),
        ("Which planet is known as the Red Planet?",
         ["Earth", "Venus", "Mars", "Jupiter"], 3),
        ("What is the chemical symbol for water?",
         ["H2O", "O2", "CO2", "H2"], 1),
    ]

    score = 0
    for question, answers, correct in quiz_questions:
        print(question)
        for i, answer in enumerate(answers, 1):
            print(f'{i}. {answer}')
        while True:
            try:
                choice = int(input('Your answer (1/2/3/4): '))
                if choice in range(1, 5):
                    break
                else:
                    print('Choose available answer number')
            except ValueError:
                print('Choose available answer number')
        if choice == correct:
            score += 1
            print('Correct!\n')
        else:
            print(f'Wrong! The correct answer was {correct}. {answers[correct - 1]}\n')

    print(f'Quiz completed! Your final score is {score}/3.')


if __name__ == '__main__':
    quiz()
