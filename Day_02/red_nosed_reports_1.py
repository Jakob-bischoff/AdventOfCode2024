def red_nosed_reports_1():
    input_data = open("test_input.txt", "r")
    data = input_data.readlines()
    safe = 0

    for row in data:
        numbers = list(map(int, row.split()))
        if is_safe(numbers):
            safe += 1

    print(safe)

def is_safe(numbers):
    counting_up = None
    for j in range(len(numbers) - 1):
        difference = numbers[j] - numbers[j + 1]
        if abs(difference) > 3 or difference == 0:
            return False

        if counting_up is None:
            counting_up = difference > 0
        elif (counting_up and difference < 0) or (not counting_up and difference > 0):
            return False

    return True


red_nosed_reports_1()
