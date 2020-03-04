from Patient import Patient
from HourlyRound import HourlyRound
from Diagnosis import Diagnosis
from ICUSystem import ICUSystem
import csv


def get_diagnosis_result(filename):
    hourly_round_list = []
    patient = None

    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        patient_row = next(reader)
        # Only extracted important attributes
        weight = patient_row[4]
        patient = Patient(patient_row[1], patient_row[2], weight)
        next(reader)
        next(reader)
        current_day = None
        for row in reader:
            day_set = None
            day = row[0]
            if day == "":
                day_set = current_day
            else:
                current_day = day
                day_set = current_day

            hourly_round_list.append(HourlyRound(day_set, row[1], row[2], row[3], row[4]))

    diagnosis = Diagnosis(patient, hourly_round_list)

    return diagnosis


icu_system = ICUSystem()
diagnosis_result_1 = get_diagnosis_result("PATIENT DATA - PATIENT A1.csv")
icu_system.add_diagnosis(diagnosis_result_1)
diagnosis_result_2 = get_diagnosis_result("PATIENT DATA - PATIENT A2.csv")
icu_system.add_diagnosis(diagnosis_result_2)
print(icu_system)


