class GRVCheck:
    def __init__(self, patient):
        self.hour = 0
        self.patient = patient

    def patient_round_decision(self, hourly_round):

        if hourly_round.grv > (self.patient.weight * 5):
            hourly_round.issues = "STOP FEEDING"

        else:
            if self.hour % 2 == 0:
                if self.patient.weight > 40:
                    hourly_round.feed = 30.0
                else:
                    hourly_round.feed = 10.0
            self.hour = self.hour + 1

        return self
