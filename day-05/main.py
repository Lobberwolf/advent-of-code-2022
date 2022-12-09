def get_stacks(filepath: str) -> dict:
    lines = open(filepath, "r").readlines()
    line_length = len(lines[0].replace("\n","")[1::4])
    stacks = {}

    for i in range(line_length+1):
        if i == 0:
            i += 1
        stacks[i] = []
        for line in lines:
            if line[1] == "1":
                break
            crate = line.replace("\n","")[1::4][i-1]
            if crate != " ":
                stacks[i].append(crate)
        stacks[i].reverse()

    return stacks
            
def get_moves(filepath: str) -> list:
    lines = open(filepath, "r").readlines()
    moves = []

    for line in lines:
        if line[0] == "m":
            line_words = line.replace("\n","").split(" ")
            move = (int(line_words[1]), int(line_words[3]), int(line_words[5]))
            moves.append(move)

    return moves

def move_crates(stacks: dict, moves: list, crane: str) -> str:
    for move in moves:
        if crane == "9000":
            for i in range(move[0]):
                stacks[move[2]].append(stacks[move[1]].pop())
        elif crane == "9001":
            bulk = []
            for i in range(move[0]):
                bulk.append(stacks[move[1]].pop())
            for i in range(move[0]):
                stacks[move[2]].append(bulk.pop())

    output = ""
    for stack in stacks.values():
        output += stack[-1]

    return output
        

def main(filepath:str, crane: str):
    stacks = get_stacks(filepath)
    moves = get_moves(filepath)
    print(move_crates(stacks, moves, crane))

if __name__ == "__main__":
    FILEPATH = "day-05/puzzle_input.txt"
    main(FILEPATH, crane="9000")
    main(FILEPATH, crane="9001")