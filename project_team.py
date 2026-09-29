from employee import Employee

class ProjectTeam:
    def __init__(self, projectCode, projectName, leader=None):
        self.__projectCode = projectCode
        self.__projectName = projectName
        self.__leader = leader
        self.__members = []

        if leader is not None:
            self.__members.append(leader)

        print(f"Project team {self.__projectCode} được tạo")

    def addMember(self, employee, makeLeader=False):

        if employee in self.__members:
            if makeLeader:
                self.__leader = employee
                print(f"{employee.getFullName()} trở thành trưởng nhóm.")

            return False

        self.__members.append(employee)
        print(f"Đã thêm {employee.getFullName()} vào nhóm.")

        if makeLeader:
            self.__leader = employee
            print(f"{employee.getFullName()} trở thành trưởng nhóm.")

        return True

    def removeMember(self, employeeId):
        for employee in self.__members:
            if employee.getId() == employeeId:
                if employee is self.__leader:
                    print(
                        f"Không thể xóa {employee.getFullName()} vì đang là trưởng nhóm"
                    )
                    print(
                        "Hãy chọn trưởng nhóm thay thế trước."
                    )
                    return

                self.__members.remove(employee)

                print(
                    f"Đã xóa {employee.getFullName()} khỏi nhóm"
                )

                return

        print(
            f"Không tìm thấy Employee có ID = {employeeId}."
        )

    def changeLeader(self, employee):
        if employee not in self.__members:
            self.__members.append(employee)
            print(f"Đã thêm {employee.getFullName()} vào danh sách thành viên")

        self.__leader = employee
        print(f"{employee.getFullName()} đã trở thành trưởng nhóm")

    def contains(self, employeeId):
        for employee in self.__members:
            if employee.getId() == employeeId:
                return True

        return False

    def calculateTotalMonthlyCost(self):
        total = 0

        for employee in self.__members:
            total += employee.calculateMonthlyCost()

        return total

    def displayTeam(self):
        print("--------------Project Team----------------")
        print(f"Project code: {self.__projectCode}")
        print(f"Project name: {self.__projectName}")

        if self.__leader is not None:
            print("\nLeader:")
            self.__leader.displayInfo()
        else:
            print("Leader: Chưa có")


        if len(self.__members) == 0:
            print("Nhóm chưa có thành viên")
        else:
            for employee in self.__members:
                print("-------------------")
                employee.displayInfo()

        print("-------------------------------------------")
        print(f"Total monthly cost: {self.calculateTotalMonthlyCost()}")

    def __del__(self):
        print(f"Project team {self.__projectCode} đã bị hủy")
