
from Question import Question

Question_prompts = [
    'What colour are apples? \n(a) Red/green \n(b) Purple \n(c) orange',
    'What colour are bananas? \n(a) Red \n(b) green \n(c) magenta',
    'What colour are strawberries? \n(a) Red \n(b) yellow \n(c) blue',
]

questions = [
    Question(Question_prompts[0], 'a'),
    Question(Question_prompts[1], 'b'),
    Question(Question_prompts[2], 'a'),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions) + ' correct')
          
run_test(questions)