class Employee:
    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0):
        if id == "":
            raise ValueError("Mã nhân sự không được rỗng!")
        if fullName == "":
            raise ValueError("Họ tên không được rỗng!")
        if baseSalary < 0:
            raise ValueError("Lương cơ bản không được âm!")

        self.__id = id
        self.__fullName = fullName
        self.__baseSalary = baseSalary

        print(f"Employee {self.__id} đã được tạo")

    def getId(self):
        return self.__id

    def getFullName(self):
        return self.__fullName

    def getBaseSalary(self):
        return self.__baseSalary

    def increaseSalary(self, value, byPercentage = False):
        if value < 0:
            raise ValueError("Giá trị tăng lương không được âm!")

        if byPercentage:
            self.__baseSalary += self.__baseSalary * value / 100
        else:
            self.__baseSalary += value

    def calculateMonthlyCost(self):
        return self.__baseSalary

    def displayInfo(self):
        print(f"Id: {self.__id}")
        print(f"Full name: {self.__fullName}")
        print(f"Base salary: {self.__baseSalary}")
        print(f"Monthly cost: {self.calculateMonthlyCost()}")

    def __del__(self):
        print(f"Employee {self.__id} đã bị xóa")
        