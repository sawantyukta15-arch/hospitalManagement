from db import get_connection

class EmployeeTerminal:

    def info_patient_main(self):
        try:
            choice = int(input(
                "**EMPLOYEE TERMINAL**\n"
                "1) View all Patients\n"
                "2) View Patients in Ascending/Descending Order\n"
                "3) View a specific Patient\n"
                "4) Filter Patients\n"
                "Enter choice: "
            ))

            match choice:
                case 1:
                    self.fetch_all()
                case 2:
                    self.fetch_sort_asc_dsc()
                case 3:
                    self.print_specific()
                case 4:
                    self.filter_within_range()
                case _:
                    print("Invalid Input")

        except ValueError:
            print("Please enter a valid number.")

    def fetch_all(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Patients")
        for row in cursor.fetchall():
            print(row)

        conn.close()

    def fetch_sort_asc_dsc(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            option = int(input("1) Ascending\n2) Descending\nChoose: "))
            column = input("Select column (age/weight): ").lower()

            if column not in ("age", "weight"):
                print("Invalid column")
                conn.close()
                return

            order = "ASC" if option == 1 else "DESC"

            cursor.execute(f"SELECT * FROM Patients ORDER BY {column} {order}")
            for row in cursor.fetchall():
                print(row)

        except ValueError:
            print("Invalid input.")

        conn.close()

    def filter_within_range(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            column = input("Filter by (age/weight): ").lower()

            if column not in ("age", "weight"):
                print("Invalid column")
                conn.close()
                return

            low = int(input("Enter lower limit: "))
            high = int(input("Enter upper limit: "))

            cursor.execute(
                f"SELECT * FROM Patients WHERE {column} BETWEEN ? AND ?",
                (low, high)
            )

            for row in cursor.fetchall():
                print(row)

        except ValueError:
            print("Limits must be numeric.")

        conn.close()

    def print_specific(self):
        conn = get_connection()
        cursor = conn.cursor()

        name = input("Enter full name of patient: ").strip()

        cursor.execute(
            "SELECT * FROM Patients WHERE name = ?",
            (name,)
        )

        rows = cursor.fetchall()
        if not rows:
            print("No patient found")
        else:
            for row in rows:
                print(row)

        conn.close()