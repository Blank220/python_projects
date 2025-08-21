#############################################################################
class Company:
    class Employee:
        def __init__(self,name,position):
            self.name = name
            self.position = position
        
        def get_details(self):
            return f'{self.name} {self.position}'

    def __init__(self,company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company1 = Company('Angels')
company2 = Company('Papa Dees')

company1.add_employee('Ate Lou','Cook')
company1.add_employee('Kuya Jack','Manager')
company1.add_employee('Ate Vista','Cashier')

company2.add_employee('Kuya Dee','Manager')
company2.add_employee('Ate Daa','Cashier')
company2.add_employee('Kuya Doo','Cook')


for employee in company1.list_employees():
    print(employee)

for employee in company2.list_employees():
    print(employee)