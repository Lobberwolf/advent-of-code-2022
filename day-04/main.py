def get_assignments(filepath: str) -> list:
    lines = open(filepath, "r").readlines()
    return [l.replace("\n","").replace("-",",").split(",") for l in lines]

def check_overlaps(assignments: list, mode: str) -> list:
    overlaps = []
    for a in assignments:
        if mode == "partial":
            if int(a[0]) >= int(a[2]) and int(a[0]) <= int(a[3]):
                overlaps.append(a)
            elif int(a[1]) >= int(a[2]) and int(a[1]) <= int(a[3]):
                overlaps.append(a)
            elif int(a[2]) >= int(a[0]) and int(a[2]) <= int(a[1]):
                overlaps.append(a)
            elif int(a[3]) >= int(a[0]) and int(a[3]) <= int(a[1]):
                overlaps.append(a)
        if mode == "complete":
            if int(a[0]) <= int(a[2]) and int(a[1]) >= int(a[3]):
                overlaps.append(a)
            elif int(a[2]) <= int(a[0]) and int(a[3]) >= int(a[1]):
                overlaps.append(a)
    return overlaps

def main(filepath: str, mode: str) -> None:
    assignments = get_assignments(filepath)
    partial_overlap_assignments = check_overlaps(assignments, mode)
    print(len(partial_overlap_assignments))

if __name__ == "__main__":
    FILEPATH = "day-04/puzzle_input.txt"

    main(FILEPATH, "partial")
    main(FILEPATH, "complete")