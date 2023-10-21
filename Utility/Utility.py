import datetime
import random

class IdGenerator:
    def __init__(self):
        self.last_timestamp = None
        self.generated_ids_in_current_second = set()

    def generate_id(self):
        # get current time in string format: yyyymmddhhmmss
        current_timestamp = datetime.datetime.now().strftime("LAL"+"%Y%m%d%H%M%S")
        
        # reset set, if current second is different from last second
        if current_timestamp != self.last_timestamp:
            self.generated_ids_in_current_second.clear()
            self.last_timestamp = current_timestamp

        # generate 4-digit random number until it is unique this second
        while True:
            rand_suffix = str(random.randint(0, 9999)).zfill(4)  # generate random 4-digit number, fill up with 0
            new_id = current_timestamp + rand_suffix
            if new_id not in self.generated_ids_in_current_second:
                self.generated_ids_in_current_second.add(new_id)
                return new_id

