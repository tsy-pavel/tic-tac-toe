def draw_board():
    print('-' * 9)
    for i in range(3):
        print('|', cells[i * 3], cells[i * 3 + 1], cells[i * 3 + 2], '|')
    print('-' * 9)

def player_turns(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def check_win():
    temp, player, count = 8, '', 0
    for i in range(0, 7, 3):
        if cells[i] == cells[i + 1] == cells[i + 2] != ' ':
            player = cells[i]; count += 1
    for i in range(3):
        if cells[i] == cells[i + 3] == cells[i + 6] != ' ':
            player = cells[i]; count += 1
    for i in range(0, 3, 2):
        temp //= 2
        if cells[i] == cells[i + temp] == cells[i + temp * 2] != ' ':
            player = cells[i]; count += 1
    return player, count

def check_coords_is_valid(coords):
    def is_numbers(coords):
        count = 0
        for coord in coords:
            if not str(coord).isdigit(): count += 1
        if count != 0:
            is_numbers(input('You should enter numbers!\nEnter the coordinates: ').split())
        return coords
    coords = is_numbers(coords)

    while not (1 <= int(coords[0]) <= 3 and 1 <= int(coords[1]) <= 3):
        coords = check_coords_is_valid(
            input('Coordinates should be from 1 to 3!\nEnter the coordinates: ').split())

    while cells[(int(coords[0]) - 1) * 3 + (int(coords[1]) - 1)] != ' ':
        coords = check_coords_is_valid(
            input('This cell is occupied! Choose another one!\nEnter the coordinates: ').split())
    
    return coords

cells, count, player = list(' ' * 9), 0, 'O'

while count != 9:
    count += 1
    player = player_turns(player)
    draw_board()
    coords = check_coords_is_valid(input('Enter the coordinates: ').split())
    cells[(int(coords[0]) - 1) * 3 + (int(coords[1]) - 1)] = player
    if count > 3: 
        win = check_win()
        if win[1] == 1:
            draw_board()
            print(win[0], 'wins')
            break
else:
    draw_board()
    print('Draw')
