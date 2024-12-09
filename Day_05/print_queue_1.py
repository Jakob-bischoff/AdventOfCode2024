def print_queue_1():
    with open("test_input.txt", "r") as file:
        input_data = file.readlines()

    rules = []
    updates = []

    for line in input_data:
        if '|' in line:
            rules.append(list(map(int,line.split('|'))))
        elif ',' in line:
            updates.append(list(map(int,line.split(','))))

    sum = 0

    for update in updates:
        middle_number = update[int((len(update)-1)/2)]
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    middle_number = 0
                    break
        sum += middle_number

    print(sum)

print_queue_1()
