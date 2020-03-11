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
        for diagnosis in self.diagnosis_list:
            state = None
            if diagnosis.patient.risk == "HR":
                state = HRDayOne(diagnosis.patient)
            else:
                state = InitialLR(diagnosis.patient)
            state_list.append(state)

        # for day in range(1, 5):
        # for day in range(1, 1):
        day = 1
        for hour in range(0, 23):
            for i in range(len(state_list)):
                patient_data = state_list[i].patient
                state_list[i] = function_name(patient_data)


                function here passing in the patient_data


                for diagnosis in self.diagnosis_list:
                    if diagnosis.patient == patient_data:
                        for hourly_round in diagnosis.hourly_rounds:
                            # if hourly_round.hour == hour and hourly_round.day == day:
                            if hour == 0 or hour == 1 and hourly_round.day == day:
                                current_state = state_list[i].patient_round_decision(hourly_round)
                                return current_state





























