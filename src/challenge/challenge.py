# Print out all of the numbers in the following array that are divisible by 3:
list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in list:
    if i % 3 == 0:
        print(i)

# The expected output for the above input is:
# 27
# 81
# 9
# 27
# 99
# 63
# 42