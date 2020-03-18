# Constructs the object ICU System with all patient objects and their respective data which is stored in a list
from HRDayOne import HRDayOne
from InitialLR import InitialLR
import datetime


class ICUSystem:
    def __init__(self):
        # Holds diagnosis for each patient (patient + hourly round data)
        self.diagnosis_list = []
        self.day = 1
        # Date time object here starting at 00:00
        self.hour = 0

    def add_diagnosis(self, diagnosis):
        self.diagnosis_list.append(diagnosis)

    def __str__(self):
        return_str = ""
        for diagnosis in self.diagnosis_list:
            return_str += str(diagnosis) + "\n"
        return return_str

    def perform_rounds(self):
        # Holds the current state of the patient
        state_list = []

        # Iterate through all diagnosis' and assign starting state
        for diagnosis in self.diagnosis_list:
            state = None
            if diagnosis.patient.risk == "HR":
                state = HRDayOne(diagnosis.patient)
            else:
                state = InitialLR(diagnosis.patient)
            state_list.append(state)

        # Iterate through each hourly reading
        for day in range(1, 5):
            for hour in range(0, 24):
                for i in range(len(state_list)):
                    # Get patient at index in state list????
                    patient_data = state_list[i].patient

                    for diagnosis in self.diagnosis_list:
                        # Check patient in diagnosis is same as stored patient
                        if diagnosis.patient == patient_data:
                            for hourly_round in diagnosis.hourly_rounds:
                                if hourly_round.time == hour and int(hourly_round.day) == day:
                                    current_state = state_list[i].patient_round_decision(hourly_round)
                                    state_list[i] = current_state




























