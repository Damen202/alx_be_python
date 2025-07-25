def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            print(f"Added '{add_item}' to the shopping list.") 
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the item to remove: ")
            if remove_item not in shopping_list:
                print(f"Item '{remove_item}' not found in the shopping list.")
            else:
                shopping_list.remove(remove_item)
                print(f"Removed '{remove_item}' from the shopping list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty. Add items to get started.")
            else:
                print(" Item(s) in your shopping list: ")
            for item in shopping_list:
                print(f"- {item}")
            #print()
            #print("End of shopping list")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()