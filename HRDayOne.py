from HRDayTwo import HRDayTwo


class HRDayOne:
    def __init__(self, patient):
        self.hour = 0
        self.patient = patient

    def patient_round_decision(self, hourly_round):
        hourly_round.feed = 1
        # Increment datetime object by 1 hour
        '''from datetime import datetime, timedelta
        az = datetime.now()
        print(az)
        az = az + timedelta(hours=1)
        print(az)'''
        self.hour = self.hour + 1

        # hour == time object 24:00
        if self.hour == 24:
            state = HRDayTwo(self.patient, hourly_round.feed)
            return state
        else:
            return self

