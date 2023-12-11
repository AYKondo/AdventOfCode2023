def get_calibration_value(line):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    primeira = ['o', 't', 'f', 's', 'e', 'n']
    terceira = ['one','two','six']
    quarta = ['four', 'five', 'nine']
    quinta = ['three', 'seven', 'eight']
    map_number = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    calibration = []
    for i, letter in enumerate(line):
        if letter in numbers:
            calibration = save_number(calibration, int(letter))
        elif letter in primeira:
            if i+4 < len(line) and line[i:i+5] in quinta:
                calibration = save_number(calibration, map_number[line[i:i+5]])
            elif i+3 < len(line) and line[i:i+4] in quarta:
                calibration = save_number(calibration, map_number[line[i:i+4]])
            elif i+2 < len(line) and line[i:i+3] in terceira:
                calibration = save_number(calibration, map_number[line[i:i+3]])

    if len(calibration) > 1:
        return calibration[0]*10 + calibration[1]
    else:
        return calibration[0]*10 + calibration[0]


def save_number(calibration, number):
    if len(calibration) <= 1:
        calibration.append(number)
    else:
        calibration[-1] = number
    return calibration

if __name__ == "__main__":
    numbers = list()
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    sum = 0
    
    for line in lines:
        sum += get_calibration_value(line)

        
    print(sum)