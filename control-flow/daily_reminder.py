# Prompt user for input
Task = input("Enter your task: ")
Time_Bound= input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

# perform a match case scenario
match Priority:
    case 'high':
        print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    case 'medium':
        print("Reminder: 'Try and finish up your project report' is a high priority task that requires immediate attention today!")
    case 'low':
        print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
if Time_Bound == 'yes':
    print("Time is still in bound")
elif Time_Bound == 'no':
    print("Time not in bound, immediate action is required based on time sensitivity")