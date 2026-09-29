from employee import Employee

class SoftwareEngineer(Employee):
    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0, primaryLanguage="UNKNOWN", technicalAllowance=0):
        super().__init__(id, fullName, baseSalary)
        self.__primaryLanguage = primaryLanguage
        self.__technicalAllowance = technicalAllowance

    def getPrimaryLanguage(self):
        return self.__primaryLanguage

    def getTechnicalAllowance(self):
        return self.__technicalAllowance

    def calculateMonthlyCost(self):
        return self.getBaseSalary() + self.__technicalAllowance

    def displayInfo(self):
        print(f"Id: {self.getId()}")
        print(f"Full name: {self.getFullName()}")
        print(f"Base salary: {self.getBaseSalary()}")
        print(f"Primary language: {self.__primaryLanguage}")
        print(f"Technical allowance: {self.__technicalAllowance}")
        print(f"Monthly cost: {self.calculateMonthlyCost()}")

    def __del__(self):
        print(f"Software engineer {self.getId()} đã bị xóa")