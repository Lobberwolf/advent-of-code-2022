"""
Opponent's Play:
A = Rock 
B = Paper
C = Scissor

Your Response:
X = Rock    = 1 point
Y = Paper   = 2 points
Z = Scissor = 3 points

Outcome:
Lose        = 0 points
Draw        = 3 points
Win         = 6 points
"""

def read_input_txt(input_path:str) -> list:
    with open(input_path, "r") as f:
        lines = f.readlines()
        input_list = []
        for line in lines:
            line = line.replace("\n", "")
            input_list.append(line.split(" "))
    return input_list

def battle_result(input:list) -> int:
    x = 1
    y = 2
    z = 3
    l = 0
    d = 3
    w = 6

    choice_x = [["A", "X", x, d], ["B", "X", x, l], ["C", "X", x, w]]
    choice_y = [["A", "Y", y, w], ["B", "Y", y, d], ["C", "Y", y, l]]
    choice_z = [["A", "Z", z, l], ["B", "Z", z, w], ["C", "Z", z, d]]

    for situation in choice_x:
        if input == situation[:2]:
            return (situation[2] + situation[3])
    for situation in choice_y:
        if input == situation[:2]:
            return (situation[2] + situation[3])
    for situation in choice_z:
        if input == situation[:2]:
            return (situation[2] + situation[3])


def calculate_battles(battles:list) -> int:
    points = 0
    for battle in battles:
        points += battle_result(battle)
    return points

battle_list = read_input_txt("input.txt")
print(calculate_battles(battle_list))