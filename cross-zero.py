def winner_check(x):
    if (matrix[0][0] == 'x' and matrix[0][1] == 'x' and matrix[0][2] == 'x' or
            matrix[1][0] == 'x' and matrix[1][1] == 'x' and matrix[1][2] == 'x' or
            matrix[2][0] == 'x' and matrix[2][1] == 'x' and matrix[2][2] == 'x' or
            matrix[0][0] == 'x' and matrix[1][0] == 'x' and matrix[2][0] == 'x' or
            matrix[0][1] == 'x' and matrix[1][1] == 'x' and matrix[2][1] == 'x' or
            matrix[0][2] == 'x' and matrix[1][2] == 'x' and matrix[2][2] == 'x' or
            matrix[0][0] == 'x' and matrix[1][1] == 'x' and matrix[2][2] == 'x' or
            matrix[0][2] == 'x' and matrix[1][1] == 'x' and matrix[2][0] == 'x'):
        print('Игрок, играющий за крестики, победил!')
        return matrix
    if (matrix[0][0] == '0' and matrix[0][1] == '0' and matrix[0][2] == '0' or
            matrix[1][0] == '0' and matrix[1][1] == '0' and matrix[1][2] == '0' or
            matrix[2][0] == '0' and matrix[2][1] == '0' and matrix[2][2] == '0' or
            matrix[0][0] == '0' and matrix[1][0] == '0' and matrix[2][0] == '0' or
            matrix[0][1] == '0' and matrix[1][1] == '0' and matrix[2][1] == '0' or
            matrix[0][2] == '0' and matrix[1][2] == '0' and matrix[2][2] == '0' or
            matrix[0][0] == '0' and matrix[1][1] == '0' and matrix[2][2] == '0' or
            matrix[0][2] == '0' and matrix[1][1] == '0' and matrix[2][0] == '0'):
        print('Игрок, играющий за нолики, победил!')
        return matrix


matrix = [
     ['*', '*', '*'],
     ['*', '*', '*'],
     ['*', '*', '*']
 ]
count = 1
player = None

while True:
    player = 'x' if count % 2 != 0 else '0'

    print(f'{count}-й ход')
    row = int(input(f'Введите строку для {player}: '))
    col = int(input(f'Введите столбец для {player}: '))

    if matrix[row - 1][col - 1] != '*':
        print('Клетка занята!')
        continue

    if (row-1) < 0 or (row-1) > 2 or (col-1) < 0 or (col-1) > 2:
        print('Выход за пределы поля!')
        continue

    matrix[row - 1][col - 1] = player
    count += 1

    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

    if winner_check(matrix):
        break

    if count == 10:
        print('Ничья, конец игры!')
        break
