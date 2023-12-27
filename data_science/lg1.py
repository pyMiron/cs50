from knights.logic import *
rain = Symbol('rain')  # its raining.
hagrid = Symbol('hagrid')  # Harry visited hagrid.
dumbledore = Symbol('dumbledore')  # Harry visited dumbledore.

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# sentence = And(rain, hagrid)

print(knowledge.formula())

