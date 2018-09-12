# create our checklist
checklist = list()

# define functions
def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + ' ' + list_item)
        index += 1

def mark_completed(index, item):
    checklist[index] = str('√' + item)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

user_value = user_input("please enter a value")
print(user_value)

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")
    return True

def test():
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run


# Run Tests
create("purple sox")
create("red cloak")

print(read(0))
print(read(1))

update(0, "purple socks")
destroy(1)

print(read(0))

list_all_items()

mark_completed(0, "purple socks")

list_all_items()

test()



running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
