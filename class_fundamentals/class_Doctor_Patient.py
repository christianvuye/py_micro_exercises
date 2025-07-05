"""
Create a medical system with Doctors and Patients that track appointments.

Requirements for Doctor class:
- Initialize with name, specialty, and empty list of patients
- Create method add_patient(patient) that adds patient to doctor's list
- Create method remove_patient(patient_name) that removes patient by name
- Create method get_patient_count() that returns number of patients
- Create method get_doctor_info() that returns doctor details and patient count

Requirements for Patient class:
- Initialize with name, patient_id, and empty list of doctors
- Create method assign_doctor(doctor) that adds doctor to patient's list
- Create method remove_doctor(doctor_name) that removes doctor by name
- Create method get_care_team() that returns list of doctor names
- Create method get_patient_summary() that returns patient info and doctors

Test your system:
doc1 = Doctor("Dr. Smith", "Cardiology")
doc2 = Doctor("Dr. Johnson", "Neurology")
patient1 = Patient("Alice", "P001")

# Establish bidirectional relationship
doc1.add_patient(patient1)
patient1.assign_doctor(doc1)
doc2.add_patient(patient1)
patient1.assign_doctor(doc2)

print(patient1.get_care_team())  # Should show both doctors
print(doc1.get_patient_count())  # Should show 1
print(patient1.get_patient_summary())  # Should show patient with both doctors
"""

class Doctor:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality
        self.patients = []
    
    def add_patient(self, patient):
        self.patients.append(patient) # add a patient instance to doctor instance
    
    def remove_patient(self, patient_name): # you want to remove the patient object, not the string
        for patient in self.patients: # for every patient object in the list of patients
            if patient.name == patient_name: # if the patient object name matches the patient_name in the param
                self.patients.remove(patient) # remove that patient object from the list of the doctors patients
                break # break the loop so there is no more compute spent on searching for that patient in the list
    
    def get_patient_count(self):
        return len(self.patients)
    
    def get_doctor_info(self):
        return f"Doctor name: {self.name}, speciality:{self.speciality}, amount of patients: {self.get_patient_count()}"
    
class Patient:
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id
        self.doctors = []

    def assign_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def remove_doctor(self, doctor_name): # same pattern as above
        for doctor in self.doctors:
            if doctor.name == doctor_name:
                self.doctors.remove(doctor)
                break
        
    def get_care_team(self): # this needs to return the name of the doctors, not the doctor objects
        return [doctor.name for doctor in self.doctors]

    def get_patient_summary(self):
        return f"Patient name: {self.name}, id:{self.patient_id}, doctors: {self.get_care_team()}"
    
# Test your system:
doc1 = Doctor("Dr. Smith", "Cardiology")
doc2 = Doctor("Dr. Johnson", "Neurology")
patient1 = Patient("Alice", "P001")

# Establish bidirectional relationship
doc1.add_patient(patient1)
patient1.assign_doctor(doc1)
doc2.add_patient(patient1)
patient1.assign_doctor(doc2)

print(patient1.get_care_team())  # Should show both doctors
print(doc1.get_patient_count())  # Should show 1
print(patient1.get_patient_summary())  # Should show patient with both doctors