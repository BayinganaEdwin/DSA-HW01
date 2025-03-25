class Sparse:
    def __init__(self, num_rows=None, num_cols=None, matrix_file_path=None):
        self.rows = 0
        self.cols = 0
        self.data = {}  # Dictionary to store non-zero values

        if matrix_file_path:
            self.load_from_file(matrix_file_path)
        elif num_rows is not None and num_cols is not None:
            self.rows = num_rows
            self.cols = num_cols
        else:
            raise ValueError("Provide either a file path or matrix dimensions")

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f]

                self.rows = self.extract_number(lines[0])
                self.cols = self.extract_number(lines[1])

                for line in lines[2:]:
                    if not line:
                        continue
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Incorrect file format")
                    row, col, value = self.convert_to_int(line[1:-1].split(','))
                    self.set_element(row, col, value)

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except ValueError as e:
            raise ValueError(f"Invalid file format: {e}")

    def extract_number(self, line):
        return int(line.split('=')[1].strip())

    def convert_to_int(self, str_list):
        return [int(s.strip()) for s in str_list]

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = Sparse(self.rows, self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.set_element(key[0], key[1], self.get_element(*key) + other.get_element(*key))
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")

        result = Sparse(self.rows, self.cols)
        for key in set(self.data.keys()).union(other.data.keys()):
            result.set_element(key[0], key[1], self.get_element(*key) - other.get_element(*key))
        return result

    def transpose(self):
        # Create a new matrix where rows and columns are swapped
        transposed = Sparse(self.cols, self.rows)

        # Set elements in the transposed matrix
        for (i, j), value in self.data.items():
            transposed.set_element(j, i, value)

        return transposed

    def multiply(self, other, max_rows=10, max_cols=10):

        result = Sparse(min(self.rows, max_rows), min(other.cols, max_cols))

        for i in range(min(self.rows, max_rows)):
            for j in range(min(other.cols, max_cols)):
                result_value = 0
                for k in range(self.cols):
                    result_value += self.get_element(i, k) * other.get_element(k, j)
                if result_value != 0:
                    result.set_element(i, j, result_value)

        return result

    def print_readable(self, max_rows=10, max_cols=10):
        print(f"Matrix size: {self.rows}x{self.cols}")
        for i in range(min(self.rows, max_rows)):
            row_str = " ".join(f"{self.get_element(i, j):5d}" for j in range(min(self.cols, max_cols)))
            print(row_str)
        if self.rows > max_rows or self.cols > max_cols:
            print("... (Truncated output for readability)")

            