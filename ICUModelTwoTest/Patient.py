# Constructs patient object with attributes from the CSV file
# Returns the attributes as strings


class Patient:
    def __init__(self, risk, age, weight):
        self.risk = risk
        self.age = age
        self.weight = weight

    def __str__(self):
        return_str = "|Patient State: " + self.risk + "|"
        return_str += self.age + "|"
        return_str += "Weight: " + str(self.weight) + "KG\n|"
        return return_str




