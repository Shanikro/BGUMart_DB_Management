from persistence import *

import sys

def add_activitie(splittedline : list[str]):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    activator_id = int(splittedline[2])
    date = splittedline[3]

    new_activitie = Activitie(product_id, quantity, activator_id, date)

    repo.activities.insert(new_activitie)

def get_quantity(id):
    result = repo.products.find(id=id)

    if result:
        return result[0].quantity
    else:
        print(f"Product with id {id} not found.")
        return None

def new_sale_or_supply(splittedline : list[str]):
    current_quantity = get_quantity(splittedline[0])

    if current_quantity + splittedline[1] >= 0:
        # Update the product quantity
        repo.products.execute_command("""
                   UPDATE products SET quantity=? WHERE id=?""",
                             (current_quantity + splittedline[1], splittedline[0]))

        # Add new activitie
        add_activitie(splittedline)


def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            if splittedline[1] != 0:
                new_sale_or_supply(splittedline[0:])

if __name__ == '__main__':
    main(sys.argv)