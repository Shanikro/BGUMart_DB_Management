from persistence import *

def main():
    print("Activities")
    activities = repo.activities.find_all_and_sord('date')
    if activities:
        for activity in activities:
            print(str(activity))

    print("Branches")
    branches = repo.branches.find_all_and_sord('id')
    if branches:
        for branche in branches:
            print(str(branche))

    print("Employees")
    employees = repo.employees.find_all_and_sord('id')
    if employees:
        for employee in employees:
            print(str(employee))

    print("Products")
    products = repo.products.find_all_and_sord('id')
    if products:
        for product in products:
            print(str(product))

    print("Suppliers")
    suppliers = repo.suppliers.find_all_and_sord('id')
    if suppliers:
        for supplier in suppliers:
            print(str(supplier))

    print()

    print("Employees report")
    command = f"""SELECT e.name, e.salary, b.location, IFNULL(total_sales, 0) AS total_sales
                    FROM employees AS e
                    JOIN branches AS b ON e.branche = b.id
                    LEFT JOIN 
                    (SELECT a.activator_id, SUM(a.quantity * p.price * -1) AS total_sales
                        FROM products AS p
                        JOIN activities AS a ON p.id = a.product_id
                        GROUP BY a.activator_id) 
                    AS sales_summary
                    ON e.id = sales_summary.activator_id
                    ORDER BY e.name ASC;
                """
    output = repo.execute_command(command)
    if output:
        for row in output:
            print(" ".join(map(str, row)))

    print("Activities report")
    command = f"""SELECT a.date, p.description, a.quantity, 
                        IFNULL(e.name, 'None') AS employee_name,
                        IFNULL(s.name, 'None') AS supplier_name 
                        
                        FROM activities AS a
                        JOIN products AS p ON a.product_id = p.id
                        LEFT JOIN employees AS e ON a.activator_id = e.id
                        LEFT JOIN suppliers AS s ON a.activator_id = s.id
                        ORDER BY a.date ASC;
                    """

    output = repo.execute_command(command)
    if output:
        for row in output:
            row_str = tuple([None if x is None else x for x in row])
            print(row_str)


if __name__ == '__main__':
    main()