import numpy as np

with open("in/02.in") as f:
    data = f.read().splitlines()

# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

def compute_remaining_cubes(row_set: str, total_available: dict) -> dict:
    # Split by category 
    row_set = [item.strip() for item in row_set.strip().split(',')]
    # Create 
    row_set: dict = {item.split(' ')[1]: int(item.split(' ')[0]) for item in row_set}

    for k, _ in row_set.items():
        total_available[k] -= row_set[k]

    return total_available

possible_games = []

# Part 1
for row in data:
    game_id = int(row.split(" ")[1].replace(":", ""))
    sets = row.split(':')[1].split(";")

    possible = []
    for _set in sets:
        total_available = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        total_available = compute_remaining_cubes(_set, total_available)
        possible.append(all([v >= 0 for v in total_available.values()]))


    if all(possible):
        possible_games.append(game_id)


print(f"Sum of possible game ids:", sum(possible_games))



# Part 2
all_powers = []
for row in data:
    game_id = int(row.split(" ")[1].replace(":", ""))
    sets = row.split(':')[1].split(";")

    all_sets = []
    for row_set in sets:
        # Split by category 
        row_set = [item.strip() for item in row_set.strip().split(',')]
        # Create 
        row_set: dict = {item.split(' ')[1]: int(item.split(' ')[0]) for item in row_set}

        all_sets.append(row_set)

    
    power_set = 1
    for k, _ in total_available.items():
        max_value = max([item.get(k, 0) for item in all_sets])
        power_set *= max_value

    all_powers.append(power_set)

print(f"Sum of each game:", sum(all_powers))