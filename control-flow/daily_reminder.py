def main():
    # Prompt for task description
    task = input("Enter your task: ").strip()

    # Prompt for priority level
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt for time-bound status
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate reminder message based on priority and time-bound status
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            print("Invalid priority level.")
            return

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
    elif time_bound == "no":
        reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound status.")
        return

    # Print the reminder message
    print(reminder)

if __name__ == "__main__":
    main()
