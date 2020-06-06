# Multiple Matrices are created to test the program
# Comment out the Matrices you do not want to use.

MATRIX = [[2.0, 4.0, 6.0],
          [1.0, 3.0, 9.0],
          [1.0, 6.0, 8.0]]

MATRIX = [[2.0, 4.0, 8.0, 2.0],
          [1.0, 2.0, 0.0, 4.0],
          [1.0, 5.0, 3.0, 0.0],
          [2.0, 7.0, 2.0, 4.0]]

MATRIX = [[2.0, 4.0, 8.0, 2.0],
          [1.0, 2.0, 0.0, 4.0],
          [1.0, 5.0, 3.0, 0.0],
          [0.0, 0.0, 0.0, 0.0]]

MATRIX = [[4.0, 8.0, 2.0],
          [2.0, 0.0, 4.0],
          [5.0, 3.0, 0.0],
          [7.0, 2.0, 4.0]]

MATRIX = [[4.0, 2.0, 5.0, 7.0],
          [8.0, 0.0, 3.0, 2.0],
          [2.0, 4.0, 0.0, 4.0]]

MATRIX = [[2.0, 0.0, 8.0, 2.0],
          [1.0, 0.0, 2.0, 4.0],
          [1.0, 0.0, 3.0, 9.0],
          [2.0, 0.0, 2.0, 6.0]]

COLUMNS = len(MATRIX[0])
ROWS = len(MATRIX)


def print_matrix():
    for i in range(ROWS):
        print(MATRIX[i])
    print()


def print_final():
    for i in range(ROWS):
        for j in range(COLUMNS):
            convert = MATRIX[i][j].as_integer_ratio()
            if convert[1] == 1:
                MATRIX[i][j] = str(convert[0])
            else:
                MATRIX[i][j] = str(convert[0]) + "/" + str(convert[1])
        print(MATRIX[i])
    print()


def swap(pos):
    # Given the row, move it down the Matrix until all the rows that do not
    # have a leading 0 in position pos, are above it
    start = pos
    check = -1
    for i in range(start, ROWS):
        if MATRIX[i][pos] != 0:
            check = 0
            print("Swapping row " + str(pos+1) + " and row " + str(i+1))
            temp = MATRIX[pos]
            MATRIX[pos] = MATRIX[i]
            MATRIX[i] = temp

            pos = i
            print_matrix()

    if check == -1:
        return False
    else:
        return True


def rre_calculator(confirm):
    r = 0
    c = 0
    check = True
    # Continue for all rows in the matrix
    while r < ROWS and c < COLUMNS:
        print("1")
        # If there is a leading 0 in a row, swap it with another row
        if MATRIX[r][c] == 0:
            check = swap(r)

        if check:
            # If there is NOT a leading one, make it a leading one
            # Whatever you do to make it a leading one, must also be done
            # to every element in the entire row
            if MATRIX[r][c] != 1 and MATRIX[r][c] != 0:
                keep = 1 / MATRIX[r][c]
                for i in range(COLUMNS):
                    MATRIX[r][i] = keep * MATRIX[r][i]
            print("Done creating pivot 1")
            print_matrix()

            # Eliminate everything below the leading 1
            for j in range(r + 1, ROWS):
                keep = -MATRIX[j][r]
                for k in range(r, COLUMNS):
                    MATRIX[j][k] = keep * MATRIX[r][k] + MATRIX[j][k]
            print("Everything below pivot is 0")
            print_matrix()
            r = r + 1
            c = c + 1
        else:
            # There is a column of 0's, so move one
            print("Column of zeros")
            c = c + 1

    # If the user only requested Row Echelon Form, return
    if confirm == 0:
        print("Matrix in Row Echelon Form")
        return

    # Otherwise, continue with Reduced Row Echelon Form
    print("Now finding Reduced Row Echelon")

    # Find the position of every 1, and eliminate everything above
    for q in range(ROWS-1, -1, -1):
        r = COLUMNS-1
        while MATRIX[q][r] != 1 and r > -1:
            r = r - 1

        # Matrix[q][r] displays the leading 1 found when reverse traversing the list
        print("Found 1, now make everything above that 1 a 0")
        print_matrix()

        for n in range(q-1, -1, -1):
            keep = -MATRIX[n][r]
            for h in range(0, COLUMNS):
                MATRIX[n][h] = keep*MATRIX[q][h] + MATRIX[n][h]

        print("Changed")
        print_matrix()
    print("Matrix in Reduced Row Echelon Form")


# # # ----- Main ----- # # #
print("What form do you want the Matrix in?")
form = input("0: Row Echelon Form\n1: Reduced Row Echelon Form\n")
rre_calculator(int(form))
print_final()

