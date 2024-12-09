def print_queue_2():
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
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    sum += reorder_update(update, rules)
                    break


    print(sum)

def reorder_update(update, rules):
    while True:
        changes_made = False
        for r in rules:
            if r[0] in update and r[1] in update:
                before = update.index(r[0])
                after = update.index(r[1])
                if before > after:
                    update[before], update[after] = update[after], update[before]
                    changes_made = True
        if not changes_made:
            break

    return update[int((len(update)-1)/2)]

print_queue_2()
