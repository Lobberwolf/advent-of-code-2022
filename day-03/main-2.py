def read_input(input_path:str)->list:
    input_list = list()
    with open(input_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            input_list.append(line.replace("\n", ""))
    return input_list

def group_input(input_list:list)->list:
    group_input_list = list()
    group = list()
    for input in input_list:
        if len(group) < 3:
            group.append(input)
        if len(group) == 3:
            group_input_list.append(group)
            group = list()

    return group_input_list

def double_input(input_list:list)->str:
    for a in input_list[0]:
        for b in input_list[1]:
            if a == b:
                for c in input_list[2]:
                    if a == c:
                        return a
    return False

def priority(input_string:str)->int:
    if input_string.isupper():
        return ord(input_string)-38
    else:
        return ord(input_string)-96
        

def main(input_path:str)->None:
    input_list = read_input(input_path)
    group_input_list = group_input(input_list)
    priority_score = 0
    for input in group_input_list:
        double = double_input(input)
        priority_item = priority(double)
        priority_score += priority_item
    print(priority_score)

    

main("input.txt")
