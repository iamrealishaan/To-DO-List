import os

# Set the background color to black
os.system("color 0f")

# To-do list program with a checklist

to_do_list = []

while True:
    print("Enter a to-do item, or press 'q' to quit.")
    new_item = input()
    
    if new_item == 'q':
        break
    
    to_do_list.append([new_item, False])
    print("Added to-do item: " + new_item)
    print("Current to-do list: ")
    for index, item in enumerate(to_do_list):
        checkbox = "[x]" if item[1] else "[ ]"
        print(str(index+1) + ". " + checkbox + " " + item[0])
    
    print("Type 'check' followed by the item number to mark an item as complete.")
    print("Type 'uncheck' followed by the item number to mark an item as incomplete.")
    print("Type 'delete' followed by the item number to delete an item.")

    command = input()
    if command.startswith("check"):
        index = int(command.split()[1]) - 1
        to_do_list[index][1] = True
    elif command.startswith("uncheck"):
        index = int(command.split()[1]) - 1
        to_do_list[index][1] = False
    elif command.startswith("delete"):
        index = int(command.split()[1]) - 1
        del to_do_list[index]

print("Goodbye!")
