import json
d= {
    "patient_id" : "123",
    "name" :"Abhinav",
    "disease" : "fever",
    "bill"  : "250",
    "room_no" : "12",
    }


with open("data.json","w") as js:
    json.dump(d,js)
    js.close()
with open("data.json","r") as js:
    patient_info=json.load(js)
    js.close()

class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        bill = input("Enter patient bill amount: ")
        room_no = input("Enter patient room no: ")

        self.patients[patient_id] = [name, disease, bill, room_no]
        print("New Patient added successfully!")

    def show_patient_info(self):
        patient_id = input("Enter patient ID: ")
        patient_info = self.patients.get(patient_id)
        print(self.patients)

        if patient_info:
            print("Patient ID:", patient_id)
            print("Name:", patient_info[0])
            print("disease:", patient_info[1])
            print("bill:", patient_info[2])
            print("room no:", patient_info[3])
        else:
            print("Patient not found.")

    def billing(self):
        patient_id = input("Enter patient ID: ")
        patient_info = self.patients.get(patient_id)
        print("do you want to modify the bill?")
    
        if patient_info:
            print("Billing details for patient", patient_info[0])
        else:
            print("Patient not found.")
# class Bill():
#     def __init__(self,billing):
#         self.billing= billing
#     def update_amount(self,new_amount):
#         self.billing=new_amount
#     def get_amount(self):
#         return self.billing
#     def updated_bill():
#         bill = float(input("enter initial amount: "))
#         bill = bill(bill)
#         print("current bill amount: ",bill.get_amount())

#         updated_amount = float(input("enter new bill: "))
#         bill.update_amount(updated_amount)
#         print("updated bill amount:",bill.get_amount())
    def bill(self):
        patient_id = input("Enter patient ID to show the bill: ")
        patient_info = self.patients.get(patient_id)
        if patient_info:
            print("Name:", patient_info[0])
            print("bill:", patient_info[2])
            update=input("Do yo want to change the bill")
            if update=="yes":
                new_bill=int(input("Enter the new amount: "))
                patient_info[2]=new_bill
                print("Bill is updated")
                
            






    def run(self):
        while True:
            print("\nHospital Management System")
            print("1. Add Patient")
            print("2. Show Patient Info")
            print("3. Billing")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == 'add':
                self.add_patient()
            elif choice == 'show':
                self.show_patient_info()
            elif choice == 'bill':
                self.bill()
            elif choice == 'exit':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__=="__main__":
    hospital_system = HospitalManagementSystem()
    hospital_system.run()
    

    


                  
                
