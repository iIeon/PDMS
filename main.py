"""
import statistics
import json
import os
import datetime

def dataAddPatient():
    print("\n-----------------------------------\n")
    enterDataName = input("Enter patient name: ")
    enterDataAge = input("Enter patient age: ")
    enterDataHeight = input("Enter patient height: ")
    enterDataWeight = input("Enter patient weight: ")
    enterDataTem = input("Enter patient temperature: ")
    enterDataBs = input("Enter the blood suger: ")
    enterDataBp = input("Enter the blood pressure: ")
    enterDataMfg = input("Enter Mfg.date: ").replace(" ", "-")
    print(f"Enter Exp.data : {datetime.date.today()}")
    print("\n-----------------------------------\n")
    enterDataNn = input("Enter the nurse name at the first station: ")
    print("\n----  List of department  ----\n1- Internal Medicine\n2- Neurology\n3- Orthopedics\n4- Ear, Nose, and Throat\n5- Cardiovascular Medicine\n6- Urology\n7- Psychiatry\n8- Obstetrics and Gynecology\n9- Pediatrics\n")
    depChoice = input("Enter the name of the department to which the patient was transferred: ")
    
    enterDataDep = ""
    if depChoice == "1":
        enterDataDep = "Internal Medicine"
    elif depChoice == "2":
        enterDataDep = "Neurology"
    elif depChoice == "3":
        enterDataDep = "Orthopedics"
    elif depChoice == "4":
        enterDataDep = "Ear, Nose, and Throat"
    elif depChoice == "5":
        enterDataDep = "Cardiovascular Medicine"
    elif depChoice == "6":
        enterDataDep = "Urology"
    elif depChoice == "7":
        enterDataDep = "Psychiatry"
    elif depChoice == "8":
        enterDataDep = "Obstetrics and Gynecology"
    elif depChoice == "9":
        enterDataDep = "Pediatrics"
    else :
        print("Faild !")
    
    enterDataDrn = input("Enter the DR name: ")
    enterDataDi = input("Enter the diagnosis: ")
    enterDataTr = input("Enter the treatment: ")


    finallyData = {
       "PatientData":{
            "Patient name": enterDataName,
            "Patient age": enterDataAge,
            "Patient height": enterDataHeight,
            "Patient weight": enterDataWeight,
            "Patient temperature": enterDataTem,
            "Patient blood suger": enterDataBs,
            "Patient pressure": enterDataBp,
            "Patient Mfg": enterDataMfg,
            "Exp": f"{datetime.date.today()}"
        },
        "Dr&Nu":{
            "Nurse name": enterDataNn,
            "Department": enterDataDep,
            "DR name": enterDataDrn,
            "Diagnosis": enterDataDi,
            "Treatment": enterDataTr
        }
    }

    key = f"Patient_{enterDataName}"

    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r", encoding="utf-8") as file:
            insertData = json.load(file)
    else:
        insertData = {}

    insertData[key.strip().lower().replace(" ", "_")] = finallyData

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(insertData, file, indent=4)
        print(f"This patient {enterDataName} has been added successfully 🟢")


def viewPatientData():
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r", encoding="utf-8") as file:
            viewData = json.load(file)
            for patKey, patData in viewData.items():
                print(f"\n{"-" * 15} Info {"-" * 15}")
                for analysisData, analysisData_data in patData.items():
                    for k, v in analysisData_data.items():
                        print(f"- {k}: {v}")
                    print("-" * 36)
                print("\n")

    else:
        print("No data is stored for any patient 🔴")


def deltePatientData():
    namePatForDelete = input("Name patient: ")
    keyPatForDelete = f"patient_{namePatForDelete}"
    
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r", encoding="utf-8") as file:
            viewDataforDelete = json.load(file)

            if keyPatForDelete in viewDataforDelete:
                print(f"Delete done for: {keyPatForDelete} 🟢")
                del viewDataforDelete[keyPatForDelete]
                with open("data.json", "w", encoding="utf-8") as fs:
                    json.dump(viewDataforDelete, fs, indent=4)
            else:
                print("There is no data on this patient 🔴")
    else:
        print("No data is stored for any patient 🔴")

def general():
    while True:
        print("----  List  ----\n1- Add patient data\n2- Delete patient data\n3- View all patients data\n4- Exit system")
        userChoice = input("Choose: ")
        if userChoice == "1":
            dataAddPatient()
        elif userChoice == "2":
            deltePatientData()
        elif userChoice == "3":
            viewPatientData()
        elif userChoice == "4":
            print("Done ✅")
            break
        else:
            print("Faild !")

general()

"""


import json
import os
import datetime

class Patient:
    def __init__(self, name, age, height, weight, temp, sugar, pressure, mfg, exp, nurse, dep, doctor, diagnosis, treatment):
        self.data = {
            "PatientData": {
                "Patient name": name,
                "Patient age": age,
                "Patient height": height,
                "Patient weight": weight,
                "Patient temperature": temp,
                "Patient blood suger": sugar,
                "Patient pressure": pressure,
                "Patient Mfg": mfg,
                "Exp": exp
            },
            "Dr&Nu": {
                "Nurse name": nurse,
                "Department": dep,
                "DR name": doctor,
                "Diagnosis": diagnosis,
                "Treatment": treatment
            }
        }
        self.key = f"patient_{name.strip().lower().replace(' ', '_')}"

class ClinicSystem:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.patients = self.load_patients()

    def load_patients(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_patients(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.patients, f, indent=4)

    def add_patient(self):
        print("\n-----------------------------------\n")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        height = input("Enter patient height: ")
        weight = input("Enter patient weight: ")
        temp = input("Enter patient temperature: ")
        sugar = input("Enter the blood suger: ")
        pressure = input("Enter the blood pressure: ")
        mfg = input("Enter Mfg.date: ").replace(" ", "-")
        exp = str(datetime.date.today())
        print(f"Enter Exp.data : {exp}")
        print("\n-----------------------------------\n")
        nurse = input("Enter the nurse name at the first station: ")
        print("\n----  List of department  ----\n1- Internal Medicine\n2- Neurology\n3- Orthopedics\n4- Ear, Nose, and Throat\n5- Cardiovascular Medicine\n6- Urology\n7- Psychiatry\n8- Obstetrics and Gynecology\n9- Pediatrics\n")
        dep_choice = input("Enter the name of the department to which the patient was transferred: ")

        dep_map = {
            "1": "Internal Medicine",
            "2": "Neurology",
            "3": "Orthopedics",
            "4": "Ear, Nose, and Throat",
            "5": "Cardiovascular Medicine",
            "6": "Urology",
            "7": "Psychiatry",
            "8": "Obstetrics and Gynecology",
            "9": "Pediatrics"
        }
        dep = dep_map.get(dep_choice, "Unknown Department")
        if dep == "Unknown Department":
            print("Faild !")
            return

        doctor = input("Enter the DR name: ")
        diagnosis = input("Enter the diagnosis: ")
        treatment = input("Enter the treatment: ")

        patient = Patient(name, age, height, weight, temp, sugar, pressure, mfg, exp, nurse, dep, doctor, diagnosis, treatment)
        self.patients[patient.key] = patient.data
        self.save_patients()
        print(f"This patient {name} has been added successfully 🟢")

    def view_patients(self):
        if self.patients:
            for patKey, patData in self.patients.items():
                print(f"\n{'-' * 15} Info {'-' * 15}")
                for section, sect_data in patData.items():
                    for k, v in sect_data.items():
                        print(f"- {k}: {v}")
                    print("-" * 36)
                print("\n")
        else:
            print("No data is stored for any patient 🔴")

    def delete_patient(self):
        name = input("Name patient: ").strip().lower().replace(' ', '_')
        key = f"patient_{name}"
        if key in self.patients:
            del self.patients[key]
            self.save_patients()
            print(f"Delete done for: {key} 🟢")
        else:
            print("There is no data on this patient 🔴")

    def run(self):
        while True:
            print("----  List  ----\n1- Add patient data\n2- Delete patient data\n3- View all patients data\n4- Exit system")
            choice = input("Choose: ")
            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.delete_patient()
            elif choice == "3":
                self.view_patients()
            elif choice == "4":
                print("Done ✅")
                break
            else:
                print("Faild !")

if __name__ == "__main__":
    clinic = ClinicSystem()
    clinic.run()
