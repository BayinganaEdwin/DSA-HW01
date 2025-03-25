import os
from sparse import Sparse

# These are the input file paths
first_sparse_matrix = '../../sample_inputs/easy_sample_03_1.txt'
second_sparse_matrix = '../../sample_inputs/easy_sample_03_2.txt'
third_sparse_matrix_three = '../../sample_inputs/easy_sample_02_2.txt'
forth_sparse_matrix = '../../sample_inputs/easy_sample_02_3.txt'

def save_result_to_file(operation, result_matrix):
    # This ensures the 'results' directory exists
    if not os.path.exists('results'):
        os.makedirs('results')
    
    # We define the filename based on the operation
    file_name = f"results/{operation}_result.txt"

    # Open the file to write the matrix result
    with open(file_name, 'w') as file:
        file.write(f"rows={result_matrix.rows}\n")
        file.write(f"cols={result_matrix.cols}\n")
        
        # Write each non-zero element of the matrix in the format (row, col, value)
        for (row, col), value in result_matrix.data.items():
            if value != 0:
                file.write(f"({row}, {col}, {value})\n")

def main():
    operation = input("Choose an operation\n1. Add\n2. Subtract\n3. Multiply\n\nChoice: ").strip().lower()

    try:
        # Load matrices
        matrix_1 = Sparse(matrix_file_path=first_sparse_matrix)
        matrix_2 = Sparse(matrix_file_path=second_sparse_matrix)
        matrix_3 = Sparse(matrix_file_path=third_sparse_matrix_three)
        matrix_4 = Sparse(matrix_file_path=forth_sparse_matrix)

        if operation == "1":
            print("\nLoading...\n")
            output = matrix_1.add(matrix_2)
            save_result_to_file("addition", output)  # Save the result to file
        elif operation == "2":
            print("\nLoading...\n")
            output = matrix_1.subtract(matrix_2)
            save_result_to_file("subtraction", output)  # Save the result to file
        elif operation == "3":
            print("\nLoading...\n")
            output = matrix_3.multiply(matrix_1, max_rows=40, max_cols=40)
            save_result_to_file("multiplication", output)  # Save the result to file
        else:
            print("Invalid operation. Please enter Add, Subtract, or Multiply.")
            return

        # Optionally, print the result (you can remove this if you only want the file)
        output.print_readable()

    except (FileNotFoundError, ValueError, IndexError) as e:
        print(f"Oops, an error occurred: {e}")
        return

if __name__ == "__main__":
    main()
