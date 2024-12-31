class AttendanceApp:

    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student name: ").strip()
        if name in self.students:
            print(f"{name} is already added.")
        else:
            self.students[name] = []
            print(f"Student {name} added successfully.")

    def mark_attendance(self):
        if not self.students:
            print("No students available. Please add students first.")
            return

        print("Mark attendance for the following students:")
        for name in self.students:
            status = input(f"Is {name} present? (y/n): ").strip().lower()
            if status == 'y':
                self.students[name].append("Present")
            elif status == 'n':
                self.students[name].append("Absent")
            else:
                print(f"Invalid input for {name}. Attendance not marked.")

        print("Attendance marked successfully.")

    def view_attendance(self):
        if not self.students:
            print("No students available. Please add students first.")
            return

        print("Attendance Records:")
        for name, records in self.students.items():
            print(f"{name}: {', '.join(records) if records else 'No records yet.'}")

    def menu(self):
        while True:
            print("\nAttendance App Menu:")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Attendance")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.mark_attendance()
            elif choice == '3':
                self.view_attendance()
            elif choice == '4':
                print("Exiting the Attendance App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = AttendanceApp()
    app.menu()
