def read_input(input_path:str)->list:
    input_list = list()
    with open(input_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            input_list.append(line.replace("\n", ""))
    return input_list

def split_input(input_list:list)->list:
    split_input_list = list()
    for input in input_list:
        split_input = list()
        input_length_half = int(len(input)/2)
        split_input.append(input[:input_length_half])
        split_input.append(input[input_length_half:])
        split_input_list.append(split_input)
    return split_input_list

def double_input(input_list:list)->str:
    for a in input_list[0]:
        for b in input_list[1]:
            if a == b:
                return a
    return False

def priority(input_string:str)->int:
    if input_string.isupper():
        return ord(input_string)-38
    else:
        return ord(input_string)-96
        

def main(input_path:str)->None:
    input_list = read_input(input_path)
    split_input_list = split_input(input_list)
    priority_score = 0
    for input in split_input_list:
        double = double_input(input)
        print(double)
        priority_item = priority(double)
        print(priority_item)
        priority_score += priority_item
    print(priority_score)

    

main("input.txt")
