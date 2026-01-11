from db import get_connection

class PatientManager:

    def patient_saving_module(self):
        try:
            self.name = input("Please input your full name:\n- ").strip()
            self.age = int(input("Please mention your age:\n- "))
            self.weight = int(input("Please describe your weight in Kgs:\n- "))
            self.condition = input("Please describe your condition:\n- ").strip()

            self.insur_status = input("Do you have insurance? (yes/no):\n- ").lower()

            if self.insur_status == "yes":
                self.insur_type = input(
                    "What type of insurance? (Government/Private):\n- "
                ).strip()
            else:
                self.insur_type = None

            self.previous_doc = input(
                "Name of the previous doctor you treated (type none if not treated):\n- "
            ).strip()

            if self.previous_doc.lower() == "none":
                self.previous_doc = None

            self.write_db()

        except ValueError:
            print("Invalid input. Age and weight must be numbers.")

    def write_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Patients
            (name, age, weight, condition, insurance_status, insurance_type, previous_doctor)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            self.name,
            self.age,
            self.weight,
            self.condition,
            self.insur_status,
            self.insur_type,
            self.previous_doc
        ))

        conn.commit()
        conn.close()

        print("Patient record saved successfully")