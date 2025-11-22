"""Some reference examples of using dictionaries."""

from typing import Dict

# Declare Dict[key_type, value_type]
team: Dict[int, str] = {}

# Insert new keys and values
team[91] = "Rodman"
team[23] = "Jordan"
team[33] = "Pippen"

# Iterate through the keys of a dictionary
for key in team:
    print(key)
    # Access values by giving their key in subscription notation
    print(team[key])

# Remove a key value pair by its key
booted_player: str = team.pop(91)
print(booted_player)
print(team)

if 23 in team:
    print("You have Jordan!")

if 91 in team:
    print("You have Rodman!")

### Change examples to DNA Base Pairs

def count_pairs(dna: str) -> Dict[str, int]:
    counts: Dict[str, int] = {
        "a": 0,
        "c": 0,
        "g": 0,
        "t": 0
    }
    for char in dna:
        counts[char] += 1
    return counts