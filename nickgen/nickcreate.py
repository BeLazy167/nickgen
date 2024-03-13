from random import choice

# Load word lists
with open('noun') as f:
    nouns = [line.rstrip() for line in f]

with open('final_adjective.txt') as f:
    adjectives = [line.rstrip() for line in f]

with open('verbs') as f:
    verbs = [line.rstrip() for line in f]

def nicke():
    # Select random words
    adjective = choice(adjectives)
    verb = choice(verbs)
    noun = choice(nouns)

    # Randomly choose between verb + noun or adjective + noun
    if choice([True, False]):
        return f"{adjective} {noun}"
    else:
        return f"{verb} {noun}"