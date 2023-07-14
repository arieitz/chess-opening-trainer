#!/usr/bin/env python
# coding: utf-8

# In[1]:



import random

openings = [
    ("Sicilian Defense", "e4 c5"),
    ("French Defense", "e4 e6"),
    ("Caro-Kann Defense", "e4 c6"),
    ("Pirc Defense", "e4 d6"),
    ("Alekhine's Defense", "e4 Nf6"),
    ("Nimzowitsch Defense", "e4 Nc6"),
    ("Owen's Defense", "e4 b6"),
    ("King's Pawn Opening", "e4 e5"),
    ("Queen's Pawn Opening", "d4 d5"),
    ("Indian Game", "d4 Nf6"),
    ("English Opening", "c4"),
    ("Zukertort Opening", "Nf3"),
    ("Van't Kruijs Opening", "e3"),
    ("Grobs Attack", "g4"),
    ("Dunst Opening", "Nc3"),
    ("Reti Opening", "Nf3 d5"),
    ("King's Indian Defense", "d4 Nf6 c4 g6"),
    ("Gruenfeld Defense", "d4 Nf6 c4 g6 Nc3 d5"),
    ("Queen's Gambit", "d4 d5 c4"),
    ("Queen's Gambit Accepted", "d4 d5 c4 dxc4"),
    ("Queen's Gambit Declined", "d4 d5 c4 e6"),
    ("Slav Defense", "d4 d5 c4 c6"),
    ("King's Gambit", "e4 e5 f4"),
    ("Italian Game", "e4 e5 Nf3 Nc6 Bc4"),
    ("Ruy-Lopez Opening", "e4 e5 Nf3 Nc6 Bb5"),
    ("Scotch Game", "e4 e5 Nf3 Nc6 d4"),
    ("Four Knights Game", "e4 e5 Nf3 Nc6 Nc3 Nf6"),
    ("Philidor Defense", "e4 e5 Nf3 d6"),
    ("Petrov Defense", "e4 e5 Nf3 Nf6"),
    ("Vienna Game", "e4 e5 Nc3"),
]

def main():
    correct = 0
    incorrect_count = 0
    incorrect = []

    
    random.shuffle(openings)
    
    total = len(openings)

    for opening in openings:
        if incorrect_count >= 3:
            print("You have given three incorrect answers. Game over.")
            return

        print(f"Moves: {opening[1]}")
        answer = input("What is the name of this opening? ")

        if answer.lower() == opening[0].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {opening[0]}.")
            incorrect.append(opening)
            incorrect_count += 1

        print()

    while len(incorrect) > 0 and incorrect_count < 3:
        print("Let's try the ones you got wrong again.")
        
        random.shuffle(incorrect)
        for opening in incorrect:
            if incorrect_count >= 3:
                print("You have given three incorrect answers. Game over.")
                return

            print(f"Moves: {opening[1]}")
            answer = input("What is the name of this opening? ")

            if answer.lower() == opening[0].lower():
                print("Correct!")
                correct += 1
                incorrect.remove(opening)
            else:
                print(f"Incorrect. The correct answer is {opening[0]}.")
                incorrect_count += 1

            print()

    print(f"Your score is {correct}/{total}.")

if __name__ == "__main__":
    main()

