# Tic-Tac-Toe
        
i=1
def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)

def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False

def check_row(cells):
    for j in range(0,3):
        if cells[j][0] == cells[j][1] == cells[j][2] !=' ':
            return True
    return False

def check_diagonal(cells):
    k=0
    if k==0:
        if cells[k][k] == cells[k+1][k+1] == cells[k+2][k+2] !=' ' or cells[k][k+2] == cells[k][k] == cells[k+2][k] !=' ':
            return True
        return False
    
def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)


player=1

while True:
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row-1][col-1] == 'x' or cells[row-1][col-1] == 'o':
        print("It is taken already")
        continue
    if player%2==1:
        cells[row-1][col-1]='x'
        player=player+1
    else:
        cells[row-1][col-1]='o'
        player=player+1
    if check(cells)== True:
        printcell(cells)
        print("Win!")
        break
    printcell(cells)
        

    
