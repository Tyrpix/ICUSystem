# Constructs the object ICU System with all patient objects and their respective data which is stored in a list
from HRDayOne import HRDayOne
from InitialLR import InitialLR


class ICUSystem:
    def __init__(self):
        self.diagnosis_list = []
        self.day = 1
        self.hour = 0

    def add_diagnosis(self, diagnosis):
        self.diagnosis_list.append(diagnosis)

    def __str__(self):
        return_str = ""
        for diagnosis in self.diagnosis_list:
            return_str += str(diagnosis) + "\n"

        return return_str

    def increment_hour(self):
        self.hour = self.hour + 1
        if self.hour == 24:
            self.hour = 0
            self.day = self.day + 1


    def perform_rounds(self):
        # Holds the state of the patient
        state_list = []

        # Starting states depending on HR or LR
        for patient in ICUSystem:
            if patient.risk == "HR":
                state = HRDayOne(patient)
            else:
                state = InitialLR(patient)

            state_list.append(state)

        for day in range(1, 5):
            for hour in range(0, 23):
                for state in state_list:
                    patient = state








