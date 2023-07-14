# N-Queens Solver
This Python program solves the classic "N-Queens" problem, where the objective is to place N queens on an NxN chessboard without them attacking each other. The program utilizes a backtracking algorithm to find all possible solutions.

## How to Use:

To use this program, follow the steps below:

1. Ensure that you have Python installed on your system (Python 3.x is recommended).
2. Copy the program code to a Python file (e.g., `n_queens.py`) or an interactive Python environment.
3. Call the `solve_n_queens(N)` function, passing the desired board size N as the argument.
4. The program will find and print all solutions for the N-Queens problem.
5. Optional: Modify the `test_solve_n_queens()` function to add or customize test cases.

## How It Works:

The program is divided into two main functions: 
`solve_n_queens(N)` and `test_solve_n_queens()`.

The `solve_n_queens(N)` function takes an integer N representing the size of the chessboard. It initializes the necessary variables and data structures, including `queens` (to track the positions of the queens), and `result` (to store the found solutions). The `is_safe()` function checks if a queen placement is safe, ensuring that no two queens threaten each other. The `place_queens()` function performs backtracking to recursively place queens on the chessboard, maintaining a valid configuration. Once all queens have been placed, a valid solution is found and appended to the `result` list.

The `test_solve_n_queens()` function provides test cases to validate the program's correctness. It compares the expected solutions with the actual solutions obtained from the `solve_n_queens(N)` function.

## Test Cases:

The program includes three test cases within the `test_solve_n_queens()` function:

1. Test Case 1: N = 4

- Verifies that the program finds two valid solutions for a 4x4 chessboard.
- Expected solutions: (1, 3, 0, 2) and (2, 0, 3, 1).
  
2. Test Case 2: N = 8

- Verifies that the program finds 92 valid solutions for an 8x8 chessboard.

3. Test Case 3: N = 0 (Edge case)

- Verifies that the program handles the edge case of N = 0 correctly, returning an empty list.

## Running the Program:

To run the program and execute the test cases:

1. Open a terminal or command prompt.
2. Navigate to the directory where the program file is located.
3. Run the program by executing the Python file.
   ```css
   python n_queens.py
   ```
- The program will display the progress and the found solutions for each test case, ensuring that the solutions match the expected results.

#### Note:  Adjust the `print()` statements within the code if you prefer a different level of verbosity or additional information during the program's execution.

**IMPORTANT!** = The program's execution time increases exponentially as N increases, so be cautious when choosing large values of N.
