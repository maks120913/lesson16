class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Ім'я: {self.name}, Посада: {self.position}, Заробітна плата: {self.salary} грн")


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Співробітник {employee.name} доданий до відділу {self.name}.")

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                print(f"Співробітник {employee_name} видалений з відділу {self.name}.")
                return
        print(f"Співробітник {employee_name} не знайдений у відділі {self.name}.")

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

    def display_department_info(self):
        print(f"Відділ: {self.name}")
        print("Список співробітників:")
        for employee in self.employees:
            print(f"{employee.name} - {employee.position}")

# Приклад використання:
employee1 = Employee("Вітковська Діана", "Менеджер", 20000)
employee2 = Employee("Басараб Максим", "Аналітик", 25000)

department = Department("Відділ розвитку")

department.add_employee(employee1)
department.add_employee(employee2)

department.display_department_info()

print("Загальна заробітна плата відділу:", department.calculate_total_salary(), "грн")

department.remove_employee("Вітковська Діана")

department.display_department_info()
