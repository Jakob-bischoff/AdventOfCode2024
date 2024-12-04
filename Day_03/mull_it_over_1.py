import re
def mull_it_over_1():
    with open("test_input.txt", "r") as file:
        input_data = file.read()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_data)
    finalNumber = 0
    for match in matches:
        first_number, second_number = map(int, match)
        finalNumber += first_number * second_number
    print(finalNumber)


mull_it_over_1()