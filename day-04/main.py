def get_assignments(filepath:str) -> list:
    f = open(filepath, "r")
    lines = f.readlines()
    assignments = [line.replace("\n","").replace("-",",").split(",") for line in lines]
    return assignments

def check_assignments(assignments:list, overlap_mode:str) -> list:
    overlap_assignments = []
    for assignment in assignments:
        if overlap_mode == "partial":
            if int(assignment[0]) >= int(assignment[2]) and int(assignment[0]) <= int(assignment[3]):
                overlap_assignments.append(assignment)
            elif int(assignment[1]) >= int(assignment[2]) and int(assignment[1]) <= int(assignment[3]):
                overlap_assignments.append(assignment)
            elif int(assignment[2]) >= int(assignment[0]) and int(assignment[2]) <= int(assignment[1]):
                overlap_assignments.append(assignment)
            elif int(assignment[3]) >= int(assignment[0]) and int(assignment[3]) <= int(assignment[1]):
                overlap_assignments.append(assignment)
        if overlap_mode == "complete":
            if int(assignment[0]) <= int(assignment[2]) and int(assignment[1]) >= int(assignment[3]):
                overlap_assignments.append(assignment)
            elif int(assignment[2]) <= int(assignment[0]) and int(assignment[3]) >= int(assignment[1]):
                overlap_assignments.append(assignment)
    return overlap_assignments

def main(filepath:str, overlap_mode:str) -> None:
    assignments = get_assignments(filepath)
    partial_overlap_assignments = check_assignments(assignments, overlap_mode)
    print(len(partial_overlap_assignments))

if __name__ == "__main__":
    FILEPATH = "day-04/puzzle_input.txt"

    main(FILEPATH, "partial")
    main(FILEPATH, "complete")