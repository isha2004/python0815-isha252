def print_unique_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()

        unique_words = sorted(set(words))
        
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print("File not found. Please make sure the file name is correct.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Prompting the user for the name of the text file
    file_name = input("Enter the name of the text file: ")

    # Printing unique words in alphabetical order
    print_unique_words(file_name)

if __name__ == "__main__":
    main()
