from tabulate import tabulate
import os

class ValueNot123Error(Exception):      #dziediczymy z klasy Exception
    """Exception raised when the value is not 1, 2, or 3."""
    def __init__(self, value, message="Value must be 1, 2, or 3"):
        self.value = value
        self.message = message
        super().__init__(f"{message}, you enter {value}")
def check_values(x, y):
    valid_values = {1, 2, 3}
    if x not in valid_values:
        raise ValueNot123Error(x)
    if y not in valid_values:
        raise ValueNot123Error(y)

def find_winner():
    # Check rows
    for row in table:
        if row[0] == row[1] == row[2] and row[0] != " ":
            exit(f"{row[0]} wins!")
    # Check columns
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] and table[0][col] != " ":
            exit(f"{table[0][col]} wins!")
    # Check diagonals
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != " ":
        exit(f"{table[0][0]} wins!")
    if table[0][2] == table[1][1] == table[2][0] and table[0][2] != " ":
        exit(f"{table[0][2]} wins!")

print("Witaj to twoja rozgrywka w tic tac toe\n");

table = [[" ", " ", " "],
         [" "," "," "],
         [" "," "," "]]
turn = True   #True X turn, False O turn

while True:
    print(tabulate(table, tablefmt="grid"))
    while True:
        print("X turn\n") if turn else print("O turn")
        try:
            x = input("Enter row: ")
            y = input("Enter column: ")
            if (x == "exit" or y == "exit"):
                exit("\nDRAW")
            x = int(x)
            y = int(y)
            check_values(x,y)
            break

        except (ValueError, NameError) as error:
            print("Incorrect value! Must be in range (1,2,3). Try again.")
        except ValueNot123Error as error:
            print(f"{error}. Try again.")

    if not table[x - 1][y - 1] == " ":
        os.system("cls")
        print("This place is already taken! Try again")
    else:
        table[x - 1][y - 1] = "X" if turn else "O"
        turn = not turn
        os.system("cls")
    find_winner()






