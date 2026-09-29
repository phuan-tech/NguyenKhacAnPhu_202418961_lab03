from employee import Employee
from software_engineer import SoftwareEngineer
from project_team import ProjectTeam

def main():
    print("=" * 60)
    print("1. TẠO HAI EMPLOYEE BẰNG HAI CONSTRUCTOR KHÁC NHAU")
    print("=" * 60)
    # Constructor 1: không truyền tham số
    employee1 = Employee()

    # Constructor 2: truyền id + fullName
    employee2 = Employee("E002", "Tran Van Binh", 5000000)

    # Constructor 3: đầy đủ 3 tham số
    employee3 = Employee("E003", "Nguyen Van An", 10000000)


    print("\nThông tin Employee:")
    employee1.displayInfo()
    print()
    employee2.displayInfo()
    print()
    employee3.displayInfo()

    print("\n" + "=" * 60)
    print("2. TẠO HAI SOFTWARE ENGINEER BẰNG HAI CONSTRUCTOR KHÁC NHAU")
    print("=" * 60)

    # Constructor với các giá trị mặc định
    engineer1 = SoftwareEngineer()

    # Constructor đầy đủ tham số
    engineer2 = SoftwareEngineer(
        "SE002",
        "Le Van Cuong",
        15000000,
        "Python",
        3000000
    )

    print("\nSoftware Engineer 1:")
    engineer1.displayInfo()

    print("\nSoftware Engineer 2:")
    engineer2.displayInfo()
    print("\n" + "=" * 60)
    print("3. TĂNG LƯƠNG MỘT NHÂN SỰ BẰNG SỐ TIỀN CỐ ĐỊNH")
    print("=" * 60)

    print("Lương trước:", employee3.getBaseSalary())

    employee3.increaseSalary(2000000)

    print("Lương sau:", employee3.getBaseSalary())


    print("\n" + "=" * 60)
    print("4. TĂNG LƯƠNG MỘT NHÂN SỰ THEO PHẦN TRĂM")
    print("=" * 60)

    print("Lương trước:", employee2.getBaseSalary())

    employee2.increaseSalary(10, True)

    print("Lương sau khi tăng 10%:", employee2.getBaseSalary())

    print("\n" + "=" * 60)
    print("5. TẠO MỘT DỰ ÁN KHÔNG CÓ TRƯỞNG NHÓM")
    print("=" * 60)

    team1 = ProjectTeam(
        "P001",
        "AI Project"
    )

    team1.displayTeam()

    print("\n" + "=" * 60)
    print("6. THÊM MỘT NHÂN SỰ VÀO NHÓM BẰNG addMember(employee)")
    print("=" * 60)

    team1.addMember(employee2)
    team1.displayTeam()

    print("\n" + "=" * 60)
    print("7. THÊM MỘT KỸ SƯ BẰNG addMember(employee, true)")
    print("=" * 60)

    team1.addMember(engineer2, True)


    print("\nThông tin nhóm sau khi thêm:")
    team1.displayTeam()

    print("\n" + "=" * 60)
    print("8. THỬ THÊM LẠI MỘT THÀNH VIÊN ĐÃ TỒN TẠI")
    print("=" * 60)

    result = team1.addMember(employee2)

    print("Kết quả:", result)

    print("\n" + "=" * 60)
    print("9. HIỂN THỊ DANH SÁCH BAO GỒM CẢ TRƯỞNG NHÓM")
    print("=" * 60)

    team1.displayTeam()

    print("\n" + "=" * 60)
    print("10. TÍNH TỔNG CHI PHÍ NHÂN SỰ HÀNG THÁNG")
    print("=" * 60)

    total = team1.calculateTotalMonthlyCost()

    print("Tổng chi phí:", total)

    print("\n" + "=" * 60)
    print("11. THỬ XÓA TRƯỞNG NHÓM HIỆN TẠI")
    print("=" * 60)

    print("Leader hiện tại là engineer2.")

    team1.removeMember("SE002")

    print("\nSau khi xóa leader:")
    team1.displayTeam()

    print("\n" + "=" * 60)
    print("12. ĐỔI TRƯỞNG NHÓM RỒI XÓA NGƯỜI TỪNG LÀ TRƯỞNG NHÓM")
    print("=" * 60)

    # Đổi leader sang employee2
    team1.changeLeader(employee2)

    print("\nLeader mới là employee2.")

    # Xóa người từng làm leader
    team1.removeMember("SE002")

    print("\nSau khi xóa người từng là leader:")
    team1.displayTeam()

    print("\n" + "=" * 60)
    print("13. MỘT NHÂN SỰ THUỘC NHIỀU NHÓM")
    print("=" * 60)

    # employee2 đang ở team1
    # Thêm employee2 vào team2

    def testTeam2():
        team2 = ProjectTeam("P002", "Web Project")
        team2.addMember(employee1)

        print("Team2 đang tồn tại:")
        team2.displayTeam()

    testTeam2()
    print("\nĐã kết thúc hàm testTeam2().")
    try:
        print(team2)
    except NameError:
        print("Team2 không còn tồn tại trong scope.")

    print("Nhân sự trong nhóm 2 vẫn còn tồn tại")
    employee1.displayInfo()
    print("--------------------------------------------")

if __name__ == "__main__":
    main()