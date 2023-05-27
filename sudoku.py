import sys
import time
from termcolor import colored

def rysuj(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                if board[i][j] == 0:
                    print(colored(" ", "red"))
                else:
                    print(colored(board[i][j], "green"))
            else:
                if board[i][j] == 0:
                    print(colored(" ", "red"), end=" ")
                else:
                    print(colored(board[i][j], "green"), end=" ")

def sprawdz(board, num, pos):
    # Sprawdza wiersz
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Sprawdza kolumnę
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Sprawdza małą siatkę 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
def puste(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
def rozwiaz(board):
    empty = puste(board)
    if not empty:
        return True
    else:
        row, col = empty
    for num in range(1, 10):
        if sprawdz(board, num, (row, col)):
            board[row][col] = num
            if rozwiaz(board):
                return True
            board[row][col] = 0
    return False

def main():

        board = [[0 for _ in range(9)] for _ in range(9)]

        print("Wprowadź planszę Sudoku. Użyj 0 dla pustych pól, nie powtarzaj liczb.")

        # Wprowadzanie danych przez gracza
        for i in range(9):
            while True:
                row_input = input(f"Wprowadź liczby dla wiersza {i+1}: ")
                if len(row_input) != 9 or not row_input.isdigit():
                    print("Niepoprawne dane. Wprowadź 9 cyfr.")
                    continue
                row = [int(num) if num.isdigit() else 0 for num in row_input]

                if row.count(1) > 1 or row.count(2) > 1 or row.count(3) > 1 or row.count(4) > 1 or row.count(5) > 1 or row.count(6) > 1 or row.count(7) > 1 or row.count(8) > 1 or row.count(9) > 1:
                    continue
                else:
                    board[i] = row
                    break

        print("\nPrzed rozwiązaniem:")
        rysuj(board)
        print("\nRozwiązywanie Sudoku...\n")

        start_time = time.time()
        if rozwiaz(board):
            end_time = time.time()
            solve_time = end_time - start_time

            print("Po rozwiązaniu:")
            rysuj(board)
            print(f"\nCzas rozwiązania: {solve_time:.2f} sekundy")
        else:
            print(colored('Nie znaleziono rozwiązania dla podanej planszy Sudoku.', 'red'))

   
     
     
while True:
    response = input("Czy chcesz rozwiązać sudoku? (Tak/Nie) ")
    if response.lower() == "tak":
        main()
    else:
        break
