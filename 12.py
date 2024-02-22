# Get input from the user
total_users = int(input("Total Users: "))
staff_users = int(input("Staff Users: "))

# Check for invalid input
if total_users < 0 or staff_users < 0 or staff_users > total_users:
    print("Invalid input. Please enter valid values.")
else:
    # Calculate the number of student users
    student_users = total_users - staff_users

    # Calculate the number of non-teaching staff users (1 for every 3 staff users)
    non_teaching_staff_users = staff_users // 3

    # Output the results
    print(f"Student Users: {student_users}")
    print(f"Non-Teaching Staff Users: {non_teaching_staff_users}")
