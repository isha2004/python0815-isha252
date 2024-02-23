

def greet(name):
    return f"Hello, {name}!"

def main():
    # Using the greet function
    name = input("Enter your name: ")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()