from persistence import *

def main():
    print("Activities")
    activities = repo.activities.find_all_and_sord('date')
    if activities:
        for activity in activities:
            print(activity.__str__)

    print("Branches")
    branches = repo.branches.find_all_and_sord('id')
    if branches:
        for branche in branches:
            print(branche.__str__)

    print("Employees")
    employees = repo.employees.find_all_and_sord('id')
    if employees:
        for employee in employees:
            print(str(employee))

    print("Products")
    products = repo.products.find_all_and_sord('id')
    if products:
        for product in products:
            print(product.__str__)

    print("Suppliers")
    suppliers = repo.suppliers.find_all_and_sord('id')
    if suppliers:
        for supplier in suppliers:
            print(supplier.__str__)

    print()
    print("Employees report")
    activities = repo.activities.find_all_and_sord('date')
    if activities:
        for activity in activities:
            print(activity.__str__)


    print("Activities report")
    activities = repo.activities.find_all_and_sord('date')
    if activities:
        for activity in activities:
            print(activity.__str__)


if __name__ == '__main__':
    main()