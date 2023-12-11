def get_calibration_value(line):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    calibration = []
    for letter in line:
        if letter in numbers:
            if len(calibration) <= 1:
                calibration.append(letter)
            else:
                calibration[-1] = letter
    if len(calibration) > 1:
        return int(calibration[0])*10 + int(calibration[1])
    else:
        return int(calibration[0])*10 + int(calibration[0])

if __name__ == "__main__":
    numbers = list()
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    sum = 0
    
    for line in lines:
        sum += get_calibration_value(line)

        
    print(sum)