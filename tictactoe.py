import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

def player_move(board):
    while True:
        try:
            row, col = map(int, input("위치를 선택하세요 (행, 열): ").split(','))
            if board[row][col] == ' ':
                return row, col
            else:
                print("이미 선택된 위치입니다. 다른 위치를 선택하세요.")
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 행과 열을 0부터 2까지의 숫자로 입력하세요.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]

    print("틱택토 게임을 시작합니다.")
    print_board(board)

    while True:
        if current_player == 'X':
            row, col = player_move(board)
        else:
            print("컴퓨터의 차례입니다.")
            row, col = computer_move(board)
            print("컴퓨터가 위치를 선택했습니다: ({}, {})".format(row, col))

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player}가 이겼습니다!")
            break
        elif all(cell != ' ' for row in board for cell in row):
            print("무승부입니다!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    main()
