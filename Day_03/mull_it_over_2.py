import re
def mull_it_over_2():
    with open("test_input.txt", "r") as file:
        input_data = file.read()

    stings = re.split(r"don't\(\)", input_data)
    filteredString = stings[0]
    for x, string in enumerate(stings[1:]):
        split_string = re.split(r"do\(\)", string)
        if len(split_string) > 1:
            split_string = split_string[1:]
            filteredString += "".join(split_string)

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, filteredString)
    finalNumber = 0
    for match in matches:
        first_number, second_number = map(int, match)
        finalNumber += first_number * second_number
    print(finalNumber)


mull_it_over_2()