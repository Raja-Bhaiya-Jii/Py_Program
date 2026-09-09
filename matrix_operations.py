"""Matrix Operations
Performs addition, subtraction, multiplication, transpose, and determinant."""
import copy

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return matrix

def print_matrix(m, label="Matrix"):
    print(f"{label}:")
    for row in m:
        print("  ", " ".join(f"{x:8.2f}" for x in row))

def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply(a, b):
    result = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def determinant(m):
    n = len(m)
    if n == 1: return m[0][0]
    if n == 2: return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c+1:] for row in m[1:]]
        det += ((-1)**c) * m[0][c] * determinant(sub)
    return det


def main():
    print("=" * 40)
    print("    MATRIX OPERATIONS")
    print("=" * 40)
    while True:
        print("\n1.Add  2.Subtract  3.Multiply  4.Transpose  5.Determinant  6.Exit")
        ch = input("Choice: ").strip()
        if ch in ('1','2','3'):
            r = int(input("Rows: ")); c = int(input("Cols: "))
            print("Matrix A:"); a = create_matrix(r, c)
            print("Matrix B:"); b = create_matrix(r, c)
            if ch == '1': print_matrix(add(a, b), "A + B")
            elif ch == '2': print_matrix(subtract(a, b), "A - B")
            else: print_matrix(multiply(a, b), "A x B")
        elif ch == '4':
            r = int(input("Rows: ")); c = int(input("Cols: "))
            a = create_matrix(r, c)
            print_matrix(transpose(a), "Transpose")
        elif ch == '5':
            n = int(input("Size (NxN): "))
            a = create_matrix(n, n)
            print(f"Determinant: {determinant(a):.2f}")
        elif ch == '6': break
        else: print("Invalid choice.")


if __name__ == "__main__":
    main()
