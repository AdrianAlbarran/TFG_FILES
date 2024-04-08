class DataCells:

    def __init__(self, number_of_processor):
        self.allCellsNewU_vector = [0]
        self.processorLens = [0] * number_of_processor

    def read_all_cells_data(self, file_name):
        try:
            with open(file_name) as file:
                lines = file.read().splitlines()
                vector_temp = [0] * int(lines[1])
                i = 0
                for line in lines:
                    if line[0] == '(' and len(line) > 2:
                        vector_temp[i] = line
                        i += 1
                self.allCellsNewU_vector = vector_temp
        except FileNotFoundError:
            print(f"File with name '{file_name}' was not found")

    def set_processor_ids(self, processor_id, processor_path):
        try:
            with open(processor_path, 'r') as file:
                lines = file.read().splitlines()
                lines = lines[19: -3]
                self.processorLens[processor_id] = [0] * int(lines[0])
                lines.pop(0)
                i = 0
                for line in lines:
                    if line[0] != '(' and line[0] != ')':
                        self.processorLens[processor_id][i] = int(line)
                        i += 1
        except FileNotFoundError:
            print(f"File with name '{processor_path}' was not found")

    def set_all_processors_id(self):
        i = 0
        for i in range(0, 6):
            path = f"processor{int(i)}/constant/polyMesh/cellProcAddressing"
            self.set_processor_ids(i, path)

    def write_all_processors(self):
        i = 0
        for i in range(0, 6):
            self.write_processor(i)

    def write_processor(self, processor_id):
        try:
            path = f"processor{int(processor_id)}/0/explicitSourceU"
            self.clean_internalfield(path)
            with open(path, 'r') as file:
                lines = file.read().splitlines(True)
                n_new_data = len(self.processorLens[processor_id])
                new_data = [str(n_new_data), '\n', '(', '\n']
                for i in range(0, n_new_data):
                    new_data.append(str(self.allCellsNewU_vector[self.processorLens[processor_id][i]]))
                    new_data.append('\n')

                new_data.append(')')
                new_data.append('\n')
                new_data.append(';')
                new_data.append('\n')
                new_file = lines[:20] + new_data + lines[20:]

            with open(path, 'w') as file2:
                file2.writelines(new_file)

        except FileNotFoundError:
            print(f"File with name '{path}' was not found")

    def clean_internalfield(self, processor_path):
        try:
            with open(processor_path, 'r') as file:

                lines = file.read().splitlines()
                old_start_lines = lines[0:20]
                lines = lines[20:]
                n_delete = int(lines[0])
                lines = lines[n_delete + 4:]

                file = old_start_lines + lines

                with open(processor_path, "w") as outFile:
                    for line in file:
                        line += "\n"
                        outFile.write(line)

        except FileNotFoundError:
            print(f"File with name '{processor_path}' was not found")


def main():
    test_class = DataCells(6)

    test_class.read_all_cells_data("data_out.txt")
    # test_class.set_processor_ids(0, "cellProcAddressing")
    test_class.set_all_processors_id()
    test_class.write_all_processors()


main()
