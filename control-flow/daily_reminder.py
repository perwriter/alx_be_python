# daily_reminder.py

# Prompt the user for the task description, priority level, and time-bound status
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on the priority and time sensitivity
reminder = f"'{task}' is a {priority} priority task"

match priority:
    case 'high':
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to complete it as soon as possible."
    case 'medium':
        if time_bound == 'yes':
            reminder += " that should be done today."
        else:
            reminder += ". Try to complete it soon."
    case 'low':
        if time_bound == 'yes':
            reminder += " that should be done today if possible."
        else:
            reminder += ". Consider completing it when you have free time."

# Print the reminder
print(f"Reminder: {reminder}")
