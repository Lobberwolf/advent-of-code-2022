def get_puzzle_inputs(filepath:str) -> list:
    puzzle_inputs = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            puzzle_inputs.append(line.replace("\n", ""))
    return puzzle_inputs

def get_grouped_inventories(inputs:list, separator:str) -> list:
    grouped_inventories = []
    inventory = []
    for input in inputs:
        if input != separator:
            inventory.append(int(input))
        else:
            grouped_inventories.append(inventory)
            inventory = []
    return grouped_inventories

def get_sum_grouped_inventories(inputs:list) -> list:
    sum_grouped_inventories = []
    for input in inputs:
        calorie_sum = 0
        for calorie in input:
            calorie_sum += calorie
        sum_grouped_inventories.append(calorie_sum)
        sum_grouped_inventories.sort()
    return sum_grouped_inventories

def get_sum_top_x_calories(inputs:list, top_x:int) -> int:
    sum_top_x_calories = 0
    for input in inputs[-top_x:]:
        sum_top_x_calories += input
    return sum_top_x_calories

def main(filepath:str, separator:str, top_x:int) -> None:
    puzzle_inputs = get_puzzle_inputs(filepath)
    grouped_inventories = get_grouped_inventories(puzzle_inputs, separator)
    sum_grouped_inventories = get_sum_grouped_inventories(grouped_inventories)
    print(get_sum_top_x_calories(sum_grouped_inventories, top_x))

if __name__ == "__main__":
    PUZZLE_INPUT_TXT = "day-01/puzzle_inputs.txt"
    SEPARATOR = ""
    TOP_X = 3
    
    main(PUZZLE_INPUT_TXT, SEPARATOR, TOP_X)