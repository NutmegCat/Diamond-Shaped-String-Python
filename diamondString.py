def print_spaces(count):
    for _ in range(count):
        print(" ", end="")

def print_pattern(input_str, spaces):
    length = len(input_str)
    pattern_length = length - spaces

    # print the left side of the pattern
    for j in range(pattern_length):
        print(input_str[j], end="")

    # print the right side of the pattern
    for j in range(pattern_length - 2, -1, -1):
        print(input_str[j], end="")

def print_diamond_pattern(input_str):
    length = len(input_str)
    total_rows = (length * 2) - 1  # calculate total number of rows
    mid_row = total_rows // 2  # calculate the middle row

    # iterate over each row
    for row in range(total_rows):
        spaces = abs(mid_row - row)  # calculate the number of spaces before the pattern

        print_spaces(spaces)
        print_pattern(input_str, spaces)

        print()  # move to the next line

should_continue = True

while should_continue:
    input_str = input("Enter a word (or type 'exit' to quit): ")

    if input_str.lower() == "exit":
        should_continue = False
    elif len(input_str) > 10:
        print("Input word is too long. Please enter another word.")
    else:
        print_diamond_pattern(input_str)