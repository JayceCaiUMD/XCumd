class Employee:
    empCount = 0
    retire = 60
    avesal = 0

    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = 'worked for {} years'.format(years)
        Employee.empCount += 1
        Employee.avesal = (Employee.avesal+salary)/Employee.empCount

    def dispCount(self):
        print('Total employee {}'.format(Employee.empCount))

    def yeartoretire(self, age):
        rest = Employee.retire - age
        print('{} years to retire'.format(rest))

    def avesalary(self):
        print('The average salary is {}'.format(Employee.avesal))


emp1 = Employee('cxy', 12345, 10)
print(emp1.name)
emp1.years
emp1.yeartoretire(30)
emp1.dispCount()
emp1.avesalary()

emp2= Employee('zxy',40000,5)
emp2.avesalary()
