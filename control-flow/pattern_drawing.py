def main():
    # Prompt the user for the size of the pattern
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row of the pattern
    while row < size:
        # Use a for loop to print asterisks for the current row
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1

if __name__ == "__main__":
    main()
