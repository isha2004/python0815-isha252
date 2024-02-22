while True:
    print("Choose an option:")
    print("1. Check if a string is a palindrome")
    print("2. Check if a number is a palindrome")
    print("0. Exit")

    choice = int(input("Enter your choice (0/1/2): "))

    if choice == 0:
        break
    elif choice == 1:
        input_str = input("Enter a string: ")
        if input_str == input_str[::-1]:
            print("Palindrome: Yes")
        else:
            print("Palindrome: No")
    elif choice == 2:
        input_num = input("Enter a number: ")
        if str(input_num) == str(input_num)[::-1]:
            print("Palindrome: Yes")
        else:
            print("Palindrome: No")
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
