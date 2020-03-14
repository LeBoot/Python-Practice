from random import choice

questions = ["Why is the sky blue? ", "Why is the grass green? ",
             "What is the meaning of life? "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because" :
    answer = input("Why? ").strip().lower()

print("Oh, okay.")
