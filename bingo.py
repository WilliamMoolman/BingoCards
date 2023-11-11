import os
import math
import random
from tqdm import tqdm

from tex_template import fourbyfour


class Card:
    def __init__(self, dimensions) -> None:
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.questions = []


# Configuration
# TODO: Make these command line arguments
NUM_CARDS = 40
CARD_DIMENSIONS = (4, 4)  # Currently only 4x4 supported, as tex template is hardcoded

# Create data folder, with subfolders for cards, texs, and pdfs
os.makedirs("data/cards", exist_ok=True)
os.makedirs("data/texs", exist_ok=True)
os.makedirs("data/pdfs", exist_ok=True)

# Read questions from questions.txt
with open("data/questions.txt", "r") as f:
    questions = [x[:-1] for x in f.readlines()]

# Create cards
print("Creating cards...")
cards = []
for i in range(NUM_CARDS):
    card = Card(CARD_DIMENSIONS)
    card.questions = random.sample(questions, CARD_DIMENSIONS[0] * CARD_DIMENSIONS[1])
    cards.append(card)
    with open(f"data/cards/card_{i}.txt", "w") as f:
        for question in card.questions:
            f.write(f"{question}\n")

# Create texs
print("Creating tex files...")
for i in range(NUM_CARDS // 2):
    with open(f"data/texs/page_{i}.tex", "w") as f:
        f.write(fourbyfour(cards[i].questions, cards[i + NUM_CARDS // 2].questions))

# Create pdfs
print("Creating pdfs...")
for i in tqdm(range(NUM_CARDS // 2)):
    os.system(
        f"pdflatex -output-directory=data/pdfs data/texs/page_{i}.tex >/dev/null 2>&1"
    )

# Merge pdfs
print("Merging pdfs...")
os.system("pdfunite data/pdfs/*.pdf data/bingo.pdf")

# Clean up
os.system("rm data/pdfs/*.aux")
os.system("rm data/pdfs/*.log")

print("Done!")
