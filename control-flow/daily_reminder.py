# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time = input("Is it time bound? yes or no: ")

# perform a match case scenario
match priority:
    case 'high':
        print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    case 'medium':
        print("Reminder: 'Try and finish up your project report' is a high priority task that requires immediate attention today!")
    case 'low':
        print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
if time == 'yes':
    print("Time is still in bound")
elif time == 'no':
    print("Time not in bound, immediate action is required based on time sensitivity")