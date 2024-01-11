from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, AKnight),
    Not(And(AKnave, AKnight)),
    Implication(And(AKnave, AKnight), AKnight),
    Implication(Not(And(AKnave, AKnight)), AKnave),

    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, BKnave),
    Or(AKnight, BKnight),
    Not(And(AKnight, BKnight)),
    Not(And(AKnave, BKnave)),
    Implication(And(AKnave, BKnave), AKnight),
    Implication(Not(And(AKnave, BKnave)), AKnave)
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, BKnave),
    Or(AKnight, BKnight),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(Or(And(AKnave, BKnave), And(AKnight, BKnight)), AKnight),
    Implication(Not(Or(And(AKnave, BKnave), And(AKnight, BKnight))), AKnave),
    Implication(And(Not(And(AKnave, BKnave)), Not(And(AKnight, BKnight))), BKnight),
    Implication(Not(And(Not(And(AKnave, BKnave)), Not(And(AKnight, BKnight)))), BKnave)
    # Implication(BKnight, AKnave),
    # Implication(AKnight, BKnave)
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, BKnave, CKnave),
    Or(AKnight, BKnight, CKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnave, CKnight)),
    Implication(Or(AKnight, AKnave), AKnight),
    BKnave,
    Implication(CKnave, BKnight),
    Implication(AKnight, CKnight),
    Implication(CKnight, AKnight)
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
