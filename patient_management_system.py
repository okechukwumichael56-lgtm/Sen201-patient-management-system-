patients = {}

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    ailment = input("Enter Ailment: ")
    ward = input("Enter Ward: ")

    patients[patient_id] = {
        "name": name,
        "ailment": ailment,
        "ward": ward
    }
    print("Patient added successfully.\n")

def view_patients():
    if not patients:
        print("No patient records available.\n")
        return

    for patient_id, details in patients.items():
        print(f"Patient ID: {patient_id}")
        print(f"Name: {details['name']}")
        print(f"Ailment: {details['ailment']}")
        print(f"Ward: {details['ward']}\n")

def update_patient():
    patient_id = input("Enter Patient ID to update: ")
    if patient_id in patients:
        patients[patient_id]["name"] = input("Enter new name: ")
        patients[patient_id]["ailment"] = input("Enter new ailment: ")
        patients[patient_id]["ward"] = input("Enter new ward: ")
        print("Patient record updated.\n")
    else:
        print("Patient not found.\n")

def delete_patient():
    patient_id = input("Enter Patient ID to delete: ")
    if patient_id in patients:
        del patients[patient_id]
        print("Patient record deleted.\n")
    else:
        print("Patient not found.\n")

def hospital_menu():
    while True:
        print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting Hospital System.")
            break
        else:
            print("Invalid option.\n")

hospital_menu()
