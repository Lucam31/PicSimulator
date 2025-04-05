import os

class FileReader:
    def __init__(self, memory):
        self.file = None
        self.memory = memory

    def readFile(self, filePath):
        try:
            with open(os.getcwd()+filePath, 'r') as file:
                self.file = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{filePath}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        self.filter_lines()
        
    def filter_lines(self) -> None:
        if self.file == None:
            raise Exception("No File was loaded!")
        filtered_lines = []
        for line in self.file:
            filtered_lines.append(line[5:9])
        k = 0
        for i in range(len(filtered_lines)):
            if filtered_lines[k].isspace():
                filtered_lines.pop(k)
            else: k+=1
        self.memory.write(filtered_lines)
        
        
    def getFile(self):
        return self.file

# Example usage:
# file_reader = FileReader('example.txt')
# filtered_lines = file_reader.read_and_filter_lines()
# print(filtered_lines)