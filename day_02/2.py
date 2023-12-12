def verify_line(line):
    max  = [12, 13, 14]
    game_sets = line.split(':')[1]
    valid = True
    minimum = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for sets in game_sets.split(';'):
        for ball in sets.split(','):
            ball_number = int(ball.split(' ')[1])
            ball_color = ball.split(' ')[2]
            if 'red' in ball_color:
                if ball_number > minimum['red']:
                    minimum['red'] = ball_number
            elif 'green' in ball_color:
                if ball_number > minimum['green']:
                    minimum['green'] = ball_number
            elif 'blue' in ball_color:
                if ball_number > minimum['blue']:
                    minimum['blue'] = ball_number
    
    if valid:
        game_number = 1
        for color in minimum:
            game_number *= minimum[color]
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