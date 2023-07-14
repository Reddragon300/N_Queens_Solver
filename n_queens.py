# Solve the classic "N-Queens" problem, where you have to place N queens on an NxN chessboard without them attacking each other.

import multiprocessing


def solve_n_queens(N):
    queens = []
    result = []

    def is_safe(queens, row, col):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def place_queens(N, row, queens):
        if row == N:
            result.append(tuple(queens[:]))
            return
        for col in range(N):
            if is_safe(queens, row, col):
                queens.append(col)
                place_queens(N, row + 1, queens)
                queens.pop()

    def solve_with_backtracking(N):
        columns = [False] * N
        diagonals1 = [False] * (2 * N - 1)
        diagonals2 = [False] * (2 * N - 1)
        place_queens(N, 0, [])

    if N == 0:
        return []

    print(f"Solving N-Queens problem for N = {N}...")

    solve_with_backtracking(N)

    print(f"Found {len(result)} solution(s):")
    for i, solution in enumerate(result):
        print(f"Solution {i+1}: {solution}")

    return result


def test_solve_n_queens():
    # Test Case 1: N = 4
    N = 4
    print(f"Running test case for N = {N}...")
    solutions = solve_n_queens(N)
    assert len(solutions) == 2
    expected_solution_1 = (1, 3, 0, 2)
    expected_solution_2 = (2, 0, 3, 1)
    assert solutions[0] in [expected_solution_1,
                            expected_solution_2], f"Actual: {solutions[0]}"
    assert solutions[1] in [expected_solution_1,
                            expected_solution_2], f"Actual: {solutions[1]}"

    # Test Case 2: N = 8
    N = 8
    print(f"Running test case for N = {N}...")
    solutions = solve_n_queens(N)
    assert len(solutions) == 92

    # Test Case 3: N = 0 (Edge case)
    N = 0
    print(f"Running test case for N = {N}...")
    solutions = solve_n_queens(N)
    assert not solutions, f"Expected: [], Actual: {solutions}"

    print("All test cases passed!")


test_solve_n_queens()
