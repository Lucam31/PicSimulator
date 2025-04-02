import os

class FileReader:
    def __init__(self, memory):
        self.file = None
        self.memory = memory

    def read_and_filter_lines(self, file_path):
        try:
            with open(os.getcwd()+file_path, 'r') as file:
                lines = file.readlines()
            filtered_lines = []
            for line in lines:
                filtered_lines.append(line[5:9])
            k = 0
            for i in range(len(filtered_lines)):
                if filtered_lines[k].isspace():
                    filtered_lines.pop(k)
                else: k+=1
            self.memory.write(filtered_lines)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        
    def getFile(self):
        return self.file

# Example usage:
# file_reader = FileReader('example.txt')
# filtered_lines = file_reader.read_and_filter_lines()
# print(filtered_lines)