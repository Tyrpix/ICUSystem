from Patient import Patient
from HourlyRound import HourlyRound
from Diagnosis import Diagnosis
from ICUSystem import ICUSystem
import datetime
import csv


def get_diagnosis_result(filename):
    hourly_round_list = []
    patient = None

    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        patient_row = next(reader)

        # Extract digits from weight, including decimal
        weight = patient_row[4]
        extracted_weight = ''.join((ch if ch in '0123456789.' else '') for ch in weight)

        # Only extracted important attributes
        patient = Patient(patient_row[1], patient_row[2], extracted_weight)
        next(reader)
        next(reader)

        # Set appropriate days if null
        current_day = None
        for row in reader:
            day_set = None
            day = row[0]
            if day == "":
                day_set = current_day
            else:
                current_day = day
                day_set = current_day

            if row[1] == '': continue
            time_obj = datetime.datetime.strptime(row[1], '%H:%M')

            hourly_round_list.append(HourlyRound(day_set, time_obj.time(), row[2], row[3], row[4]))

    diagnosis = Diagnosis(patient, hourly_round_list)

    return diagnosis


icu_system = ICUSystem()
diagnosis_A1 = get_diagnosis_result("PATIENT DATA - PATIENT A1.csv")
icu_system.add_diagnosis(diagnosis_A1)
diagnosis_A2 = get_diagnosis_result("PATIENT DATA - PATIENT A2.csv")
icu_system.add_diagnosis(diagnosis_A2)
icu_system.perform_rounds()
print(icu_system)



