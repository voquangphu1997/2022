def print_menu():
    print("""
    Enter your selection: 
    1. View production list
    2. Add a new production to the list
    3. Edit the name of the production in list
    4. Remove a production from the list
    5. Exit
 """)
list = {
        'a001': "book",
        'a002': "cup",
        'a003': "laptop",
        'a004': "table",
        'a005': "chair",
    }
def view_product_list():
    print(list)

def add_new_product_to_list():
    product_id = input("Enter the id of product: ")
    product_name = input("Enter the name of product: ")
    if product_id in list:
        print("Product ID is avaiable")
        print("You can choose the 3rd option to edit the product name")
    else:
        list[product_id] = product_name
        print(list)
def edit_name_product_to_list():
    product_id = input("Enter the id of product: ")
    product_name = input("Enter the name of product: ")
    list[product_id] = product_name
    print(list)
def remove_product_from_list():
    product_id = input("Enter the id of product: ")
    if product_id in list:
        list.pop(product_id)
        print(list)
    else:
        print("Product ID is unavaiable to remove")
        print("You can choose the 3rd option to edit the product name")
while True:
    print_menu()
    user_input = int(input("choose your option: "))
    if user_input == 1:
        view_product_list()
    elif user_input == 2:
        add_new_product_to_list()
    elif user_input == 3:
        edit_name_product_to_list()
    elif user_input == 4:
        remove_product_from_list()
    elif user_input == 5:
        break
    
