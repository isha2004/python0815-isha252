# Given information
pa = 28  # person's age at younger brother 24
db = 4   # age difference between person and younger brother
ob = 56  # older brother's age at 56

# Calculate age difference when older brother is 56
dob_56 = ob - (pa + db)

# Check if age difference is more than 3
if dob_56 > 3:
    # Calculate age of younger brother when older brother was 5
    yb_5 = pa - (ob - 5)
    print(f"Younger brother's age when the older brother was 5: {yb_5}")
else:
    print("The age difference when the older brother is 56 is not more than 3.")
