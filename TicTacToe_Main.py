# наше поле с подписанными ячейками
board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]


def print_board(board):
    # добавляем вертикальных палочек чтоб красиво было
    for row in board:
        print(" | ".join(row))


def check_win(board, player):
    # проверяем условие победы
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def check_draw(board):
    # проверяем на ничью
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True


def get_coordinates(cell_number):
    # чтоб игрокам печатать не 2 числа а 1 делаем словарь)
    move = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
    }
    return move.get(cell_number, None)


def game():
    current_player = "X"

    while True:
        print_board(board)  # сначала печатаем поле
        cell_number = input(f"Игрок {current_player} выберите незанятое поле от 1 до 9: ")  # получаем от игрока число
        position = get_coordinates(cell_number)  # через функцию get_coordinates получаем координаты по ключу

        # проверяем занята ли ячейка по полученным координатам
        if position is None or board[position[0]][position[1]] in ['X', 'O']:
            print("Либо вы выбрали уже занятое поле, либо опечатались, выберите незанятое поле от 1 до 9")
            continue

        board[position[0]][position[1]] = current_player  # если все удалось то обновляем поле

        # проверяем победу
        if check_win(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил")
            break

        # проверяем ничью
        if check_draw(board):
            print_board(board)
            print("Ничья")
            break

        # если игра не закончилась, передаем ход, меняем игрока
        current_player = "O" if current_player == "X" else "X"


game()
