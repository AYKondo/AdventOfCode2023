def verify_line(line):
    max  = [12, 13, 14]
    game_number = int(line.split(':')[0].split(' ')[1])
    game_sets = line.split(':')[1]
    valid = True
    for sets in game_sets.split(';'):
        for ball in sets.split(','):
            if 'red' in ball and int(ball.split(' ')[1]) > max[0]:
                valid = False
            elif 'green' in ball and int(ball.split(' ')[1]) > max[1]:
                valid = False
            elif 'blue' in ball and int(ball.split(' ')[1]) > max[2]:
                valid = False
    
    if valid:
        return game_number
    else:
        return 0


if __name__ == "__main__":
    numbers = list()
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    sum = 0
    
    for line in lines:
        sum += verify_line(line)

        
    print(sum)