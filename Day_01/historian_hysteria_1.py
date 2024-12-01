def historian_hysteria_1():
    input_data = open("input.txt", "r")
    data = input_data.readlines()
    leftside = []
    rightside = []
    for i in data:
        left_id = int(i.split("  ")[0])
        right_id = int(i.split("  ")[1])
        leftside.append(left_id)
        rightside.append(right_id)
    leftside.sort()
    rightside.sort()
    total_distance = 0
    for i in range(len(leftside)):
      total_distance += abs(rightside[i] - leftside[i])
    print(total_distance)

historian_hysteria_1()