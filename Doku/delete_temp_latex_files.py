import os
import glob

def delete_temp_latex_files(directory):
    # Define file extensions to delete
    temp_extensions = [
        '*.aux', '*.log', '*.out', '*.toc', '*.fdb_latexmk', '*.fls'
    ]

    # Iterate over each extension and delete matching files
    for ext in temp_extensions:
        for file in glob.glob(os.path.join(directory, ext)):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

if __name__ == "__main__":
    # Specify the directory containing LaTeX files
    latex_directory = "/Users/leandergantert/Documents/Projekte/Python/PicSimulator/Doku"
    delete_temp_latex_files(latex_directory)