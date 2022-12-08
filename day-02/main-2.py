"""
Opponent's Play:
A = Rock 
B = Paper
C = Scissor

Your Response:
Rock        = 1 point
Paper       = 2 points
Scissor     = 3 points

Outcome:
X = Lose    = 0 points
Y = Draw    = 3 points
Z = Win     = 6 points
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
    r = 1
    p = 2
    s = 3
    x = 0
    y = 3
    z = 6

    choice_x = [["A", "X", x, s], ["B", "X", x, r], ["C", "X", x, p]]
    choice_y = [["A", "Y", y, r], ["B", "Y", y, p], ["C", "Y", y, s]]
    choice_z = [["A", "Z", z, p], ["B", "Z", z, s], ["C", "Z", z, r]]

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