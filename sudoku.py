import sys
import time

def rysujtablice(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" ", end=" ")
                else:
                    print(board[i][j], end=" ")

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

def wprowadz_liczbe(prompt):
    while True:
        liczba = input(prompt)
        if not liczba.isdigit():
            print("Wprowadź poprawną liczbę.")
        else:
            liczba = int(liczba)
            if liczba < 0 or liczba > 9 :
                print("Wprowadź liczbę od 0 do 9.")
            else:
                return liczba

def start():
    board = [[0 for _ in range(9)] for _ in range(9)]
    print("Wprowadź planszę Sudoku. Użyj 0 dla pustych pól.")

    # wprowadzanie danych przez gracza
    for i in range(9):
        while True:
            row_input = input(f"Wprowadź liczby dla wiersza {i+1}: ")
            if len(row_input) != 9 or not row_input.isdigit():
                print("Niepoprawne dane. Wprowadź 9 cyfr.")
                continue
            row = [int(num) for num in row_input]

            if len(set(row)) != len(row) and row.count(0) != len(row) - 1:
                print("Niepoprawne dane. Wprowadzona linia zawiera powtórzone liczby.")
                continue
            else:
                board[i] = row
                break

    print("\nPrzed rozwiązaniem:")
    rysujtablice(board)
    print("\nRozwiązywanie Sudoku...\n")

    start_time = time.time()
    if puste(board):
        end_time = time.time()
        puste_time = end_time - start_time

        print("Po rozwiązaniu:")
        rysujtablice(board)
        print(f"\nCzas rozwiązania: {puste_time:.2f} sekundy")
    else:
        print("Nie znaleziono rozwiązania dla podanej planszy Sudoku.")

while True:
    response = input("Czy chcesz rozwiązać sudoku? (Tak/Nie) ")
    if response.lower() == "tak":
        start()
    else:
        break
