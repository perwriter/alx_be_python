def main():
    # Prompt the user for a number
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate and print the multiplication table
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
