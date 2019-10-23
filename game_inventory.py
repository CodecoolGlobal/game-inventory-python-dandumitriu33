
import csv

# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    for i in inventory.items():
        print(f'{i[0]}: {i[1]}')


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        elif i not in inventory.keys():
            inventory[i] = 1
    return inventory


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''

    key_lengths = []
    for i in inventory.keys():
        key_lengths.append(len(i))  
    key_lengths.append(len('item name'))
    item_name_column_width = int(max(key_lengths))
    value_lengths = []
    for j in inventory.values():
        value_lengths.append(len(str(j)))
    value_lengths.append(len('count'))
    item_count_column_width = int(max(value_lengths))
    table_width = item_name_column_width + item_count_column_width + 3  # the |
    print('-' * table_width)
    print('{:{align}{width}} |'.format('item name', align='>', width=str(item_name_column_width)),
          '{:{align}{width}}'.format('count', align='>', width=str(item_count_column_width)))
    print('-' * table_width)

    def print_inventory_normal():
        for i in range(len(inventory)):
            print('{:{align}{width}} |'.format(list(inventory.keys())[i], align='>', width=str(item_name_column_width)),
                  '{:{align}{width}}'.format(list(inventory.values())[i], align='>', width=str(item_count_column_width)))

    def print_inventory_ascending():
        sorted_inventory_tuples = sorted(inventory.items(), key=lambda kv: kv[1])
        # print(sorted_inventory_tuples)
        for i in sorted_inventory_tuples:
            print('{:{align}{width}} |'.format(i[0], align='>', width=str(item_name_column_width)),
                  '{:{align}{width}}'.format(i[1], align='>', width=str(item_count_column_width)))

    def print_inventory_descending():
        reverse_sorted_inventory_tuples = reversed(sorted(inventory.items(), key=lambda kv: kv[1]))
        for i in reverse_sorted_inventory_tuples:
            print('{:{align}{width}} |'.format(i[0], align='>', width=str(item_name_column_width)),
                  '{:{align}{width}}'.format(i[1], align='>', width=str(item_count_column_width)))

    if order == 'count,asc':
        print_inventory_ascending()
    elif order == 'count,desc':
        print_inventory_descending()
    else:
        print_inventory_normal()
    print('-' * table_width)


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''
    try:
        with open(filename, 'rt', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for i in row:
                    if i in inventory:
                        inventory[i] += 1
                    else:
                        inventory[i] = 1
    except FileNotFoundError:
        print("File 'no_such_file.csv' not found!")
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''
    item_list = []
    for key in inventory.keys():
        for i in range(inventory[key]):
            item_list.append(key)
    try:
        with open(filename, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(item_list)
    except PermissionError:
        print("You don't have permission creating file '/nopermission.csv'!")    
