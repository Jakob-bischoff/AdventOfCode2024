def historian_hysteria_2():
    input_data = open("test_input.txt", "r")
    data = input_data.readlines()
    leftside = []
    rightside = []
    for i in data:
        left_id = int(i.split("  ")[0])
        right_id = int(i.split("  ")[1])
        leftside.append(left_id)
        rightside.append(right_id)
    score = 0
    for i in range(len(leftside)):
        main_number =  leftside[i]
        main_number_right = rightside.count(main_number)
        score += int(main_number) * main_number_right

    print(score)
historian_hysteria_2()