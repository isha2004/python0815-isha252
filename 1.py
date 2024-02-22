def find_lsd_msd(num):
    # LSD (Least Significant Digit)
    lsd = num % 10
    
    # MSD (Most Significant Digit)
    while num >= 10:
        num //= 10
    msd = num
    
    return lsd, msd

# Input number
number = 1010101

# Find LSD and MSD
lsd, msd = find_lsd_msd(number)

# Output results
print(f"Input: {number}")
print(f"MSD: {msd}")
print(f"LSD: {lsd}")