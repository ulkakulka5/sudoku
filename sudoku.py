import sys
import time
from termcolor import colored #na internecie znalazłam taką biblioteke do kolorow

def rysujtablice(board):
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
    # sprawdza wiersz
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # sprawdza kolumnę
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # sprawdza małą siatkę 3x3
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

def start():
    board = [[0 for _ in range(9)] for _ in range(9)]
    print("Wprowadź planszę Sudoku. Użyj 0 dla pustych pól.")

    # Wprowadzanie danych przez gracza
    for i in range(9):
        row_input = input(f"Wprowadź liczby dla wiersza {i+1}: ")
        for j in range(9):
            if row_input[j].isdigit():
                board[i][j] = int(row_input[j])

    print("\nPrzed rozwiązaniem:")
    rysujtablice(board)
    print("\nRozwiązywanie Sudoku...\n")

    start_time = time.time()
    if rozwiaz(board):
        end_time = time.time()
        rozwiaz_time = end_time - start_time

        print("Po rozwiązaniu:")
        rysujtablice(board)
        print(f"\nCzas rozwiązania: {rozwiaz_time:.2f} sekundy")
    else:
        print("Nie znaleziono rozwiązania dla podanej planszy Sudoku.")

while True:
    response = input("Czy chcesz rozwiązać sudoku? (Tak/Nie) ")
    if response.lower() == "tak":
        start()
    else:
        break