# Prompt user for input
task_variable = input("Enter your task: ")
task_priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time bound? yes or no: ")

# perform a match case scenario
match task_priority:
    case 'high':
        print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    case 'medium':
        print("Reminder: 'Try and finish up your project report' is a high priority task that requires immediate attention today!")
    case 'low':
        print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
if time_bound == 'yes':
    print("Time is still in bound")
elif time_bound == 'no':
    print("Time not in bound, immediate action is required based on time sensitivity")