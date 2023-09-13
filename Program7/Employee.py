class Employee :
    def __init__(self):
        self.empname = ""
        self.empId = " "
        self.salary = " "
        self.department = ""
    
    def getDetails(self):
        self.empname = input("Enter the name of the employee :")
        self.empId = input("Enter the employee ID :")
        self.salary = input("Enter the salary of the employee :")
        self.department = input("Enter the employee department:")
    
    def showDetails(self):
        print("Employee Name :",self.empname)
        print("Employee ID :", self.empId)
        print("Department :", self.department)
        print("Saary : ", self.salary)
    
    def updateSalary(self):
        self.salary = input("Enter the updated salary")
        print("Updated salary is : ", self.salary)

emp = Employee()
emp.getDetails()
emp.showDetails()
emp.updateSalary()
emp.showDetails()