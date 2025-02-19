from sparse import Sparse

first_sparse_matrix = '../../sample_inputs/easy_sample_03_1.txt'
second_sparse_matrix = '../../sample_inputs/easy_sample_03_2.txt'
third_sparse_matrix_three = '../../sample_inputs/easy_sample_02_2.txt'
forth_sparse_matrix = '../../sample_inputs/easy_sample_02_3.txt'

def main():
    

    operation = input("Choose an operation\n1. Add\n2. Subtract\n3. Multiply\n\nChoice: ").strip().lower()

    try:
        matrix_1 = Sparse(matrix_file_path=first_sparse_matrix)
        matrix_2 = Sparse(matrix_file_path=second_sparse_matrix)
        matrix_3 = Sparse(matrix_file_path=third_sparse_matrix_three)
        matrix_4 = Sparse(matrix_file_path=forth_sparse_matrix)

        if operation == "1":
            print("\nLoading...\n")
            output = matrix_1.add(matrix_2)
        elif operation == "2":
            print("\nLoading...\n")
            output = matrix_1.subtract(matrix_2)
        elif operation == "3":
            print("\nLoading...\n")
            output = matrix_3.multiply(matrix_4)
        else:
            print("Invalid operation. Please enter Add, Subtract, or Multiply.")
            return

        output.print_readable()
    
    except (FileNotFoundError, ValueError, IndexError) as e:
        print(f"Oops, an error occured: {e}")
        return

if __name__ == "__main__":
    main()
