# Constructs hourly round object with attributes from the CSV file based on each row per hour
# Returns the attributes as strings


class HourlyRound:
    def __init__(self, day, time, feed, grv, issues):
        self.day = day
        self.time = time
        self.feed = feed
        self.grv = grv
        self.issues = issues

    def __str__(self):
        return_str = "|Day: " + self.day
        return_str += "|Time: " + str(self.time) + ":00"
        return_str += "|Feed: " + str(self.feed)
        return_str += "|GRV: " + str(self.grv)
        return_str += "|Issues: " + self.issues + "|\n"
        return return_str
