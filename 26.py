# copyfile.py

def copy_file_content(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("File not found. Please make sure the file names are correct.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Prompting the user for file names
    source_file = input("Enter the name of the source text file: ")
    destination_file = input("Enter the name of the destination text file: ")

    # Copying contents from the source file to the destination file
    copy_file_content(source_file, destination_file)

if __name__ == "__main__":
    main()
